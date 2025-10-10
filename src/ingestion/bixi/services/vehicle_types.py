import logging

import requests
from ingestion.bixi.settings import BixiSettings

logging.getLogger(__name__)


class VehicleTypes:
    def __init__(self) -> None:
        self.settings = BixiSettings()

    def fetch(self):
        url = self.settings.vehicle_types_url
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error fetching vehicle types: {e}")
            return None

    def load(self, data: list[dict]):
        pass