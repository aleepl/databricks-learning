import logging
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import List

import requests
from utils.s3_tools import S3Bucket

from ingestion.bixi.models.system_alerts import SystemAlerts
from ingestion.bixi.settings import BixiSettings

logger = logging.getLogger(__name__)


@dataclass
class SystemAlertsRepsonse:
    last_updated: int
    ttl: int
    version: str
    data: List[SystemAlerts]


@dataclass
class SystemAlertsService:
    def __init__(self, settings) -> None:
        self._settings = BixiSettings()

    def fetch(self) -> SystemAlertsRepsonse | None:
        url = self._settings.station_info_url
        try:
            logger.info("Fetching system alerts.")
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            data = response.json()
            return SystemAlertsRepsonse(**data)
        except requests.RequestException as e:
            logger.error(f"Error fetching system alerts: {e}")
            return

    def load(self, bucket_name, data: SystemAlertsRepsonse | None, timestamp: datetime = datetime.now()) -> None:
        if data is None:
            logger.warning("No station data to load; skipping S3 upload.")
            return

        logger.info("Loading system alerts.")
        # Prepare filename and data payload
        year, month, day = (
            timestamp.year, timestamp.month, timestamp.day
        )
        unix_timestamp = int(timestamp.timestamp())

        # Load data to S3
        filename = Path("system_alerts", f"year={year}", f"month={month}", f"day={day}", f"{unix_timestamp}.json")
        s3 = S3Bucket(bucket_name)
        s3.load(filename.as_posix(), asdict(data))
