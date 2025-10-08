import logging

import requests
from ingestion.bixi.settings import BixiSettings

logging.getLogger(__name__)


class SystemAlerts:
    def __init__(self) -> None:
        self.settings = BixiSettings()

    def fetch(self):
        url = self.settings.system_alerts_url
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error fetching system alerts: {e}")
            return None

    def load(self, data: list[dict]):
        pass