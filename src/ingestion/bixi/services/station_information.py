import logging
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import List

import requests

from ingestion.bixi.models.station import Station
from utils.s3_tools import S3Bucket

logger = logging.getLogger(__name__)


@dataclass
class StationInfoData:
    stations: List[Station]

@dataclass
class StationInfoResponse:
    last_updated: int
    ttl: int
    version: str
    data: StationInfoData


class StationInfoService:
    def __init__(self, settings) -> None:
        self._settings = settings

    def fetch(self) -> StationInfoResponse | None:
        url = self._settings.station_info_url
        try:
            logger.info("Fetching station information.")
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            data = response.json()
            return StationInfoResponse(**data)
        except requests.RequestException as e:
            logger.error(f"Error fetching station information: {e}")
            return

    def load(self, bucket_name, data: StationInfoResponse | None, timestamp: datetime = datetime.now()) -> None:
        if data is None:
            logger.warning("No station data to load; skipping S3 upload.")
            return

        logger.info("Loading station information.")
        # Prepare filename and data payload
        year, month, day = (timestamp.year, timestamp.month, timestamp.day)
        unix_timestamp = int(timestamp.timestamp())

        # Load data to S3
        filename = Path("ingestion","station_info", f"year={year}", f"month={month}", f"day={day}", f"{unix_timestamp}.json")
        s3 = S3Bucket(bucket_name)
        s3.load(filename.as_posix(), asdict(data))
