import logging
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import List

import requests

from ingestion.bixi.models.vehicule_type import VehiculeType
from ingestion.bixi.settings import BixiSettings
from utils.s3_tools import S3Bucket

logger = logging.getLogger(__name__)


@dataclass
class VehicleTypesResponse:
    last_updated: int
    ttl: int
    version: str
    data: List[VehiculeType]


class VehicleTypesService:
    def __init__(self, settings) -> None:
        self._settings = BixiSettings()

    def fetch(self) -> VehicleTypesResponse | None:
        url = self._settings.station_info_url
        try:
            logger.info("Fetching vehicule types.")
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            data = response.json()
            return VehicleTypesResponse(**data)
        except requests.RequestException as e:
            logger.error(f"Error fetching vehicule types: {e}")
            return

    def load(self, bucket_name, data: VehicleTypesResponse | None, timestamp: datetime = datetime.now()) -> None:
        if data is None:
            logger.warning("No station data to load; skipping S3 upload.")
            return

        logger.info("Loading vehicule types.")
        # Prepare filename and data payload
        year, month, day = (timestamp.year, timestamp.month, timestamp.day)
        unix_timestamp = int(timestamp.timestamp())

        # Load data to S3
        filename = Path("ingestion", "vehicule_types", f"year={year}", f"month={month}", f"day={day}", f"{unix_timestamp}.json")
        s3 = S3Bucket(bucket_name)
        s3.load(filename.as_posix(), asdict(data))
