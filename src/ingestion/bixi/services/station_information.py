import logging
from datetime import datetime
from pathlib import Path
from typing import List

import requests

from ingestion.bixi.settings import BixiSettings
from utils.s3_tools import S3Bucket
from dataclasses import dataclass, asdict
from ingestion.bixi.models.station import Station

@dataclass
class StationInfoResponse:
    last_updated: int
    ttl: int
    version: str
    data: List[Station]

class StationInfoService:
    def __init__(self) -> None:
        self.settings = BixiSettings()

    def fetch(self) -> StationInfoResponse | None:
        url = self.settings.station_info_url
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            data = response.json()
            return StationInfoResponse(**data)
        except requests.RequestException as e:
            logging.error(f"Error fetching station information: {e}")
            return

    def load(self, bucket_name, data: StationInfoResponse | None, timestamp: datetime = datetime.now()) -> None:
        if data is None:
            logging.warning("No station data to load; skipping S3 upload.")
            return
    
        # Prepare filename and data payload
        year, month, day = (
            timestamp.year, timestamp.month, timestamp.day
        )
        unix_timestamp = int(timestamp.timestamp())

        # Load data to S3
        filename = Path("station_info", f"year={year}", f"month={month}", f"day={day}", f"{unix_timestamp}.json")
        s3 = S3Bucket(bucket_name)
        s3.load(filename.as_posix(), asdict(data))

if __name__ == "__main__":
    bucket_name = "databricks-playground-bucket-20251003"
    station_info = StationInfoService()
    data = station_info.fetch()
    station_info.load(bucket_name, data)
