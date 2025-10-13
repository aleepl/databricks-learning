import logging
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import List

import requests
from utils.s3_tools import S3Bucket

from ingestion.bixi.models.station_status import StationStatus

logger = logging.getLogger(__name__)


@dataclass
class StationStatusResponse:
    last_updated: int
    ttl: int
    version: str
    data: List[StationStatus]


class StationStatusService:
    def __init__(self, settings) -> None:
        self._settings = settings

    def fetch(self) -> StationStatusResponse | None:
        url = self._settings.station_info_url
        try:
            logger.info("Fetching station status.")
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            data = response.json()
            return StationStatusResponse(**data)
        except requests.RequestException as e:
            logger.error(f"Error fetching station status: {e}")
            return

    def load(self, bucket_name, data: StationStatusResponse | None, timestamp: datetime = datetime.now()) -> None:
        if data is None:
            logger.warning("No station data to load; skipping S3 upload.")
            return

        logger.info("Loading station status.")
        # Prepare filename and data payload
        year, month, day = (
            timestamp.year, timestamp.month, timestamp.day
        )
        unix_timestamp = int(timestamp.timestamp())

        # Load data to S3
        filename = Path("station_status", f"year={year}", f"month={month}", f"day={day}", f"{unix_timestamp}.json")
        s3 = S3Bucket(bucket_name)
        s3.load(filename.as_posix(), asdict(data))
