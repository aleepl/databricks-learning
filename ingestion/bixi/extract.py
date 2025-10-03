import requests
from .settings import BixiSettings
import logging


class Bixi:
    def __init__(self) -> None:
        self.settings = BixiSettings()
    
    def _fetch_vehicle_types(self):
        url = self.settings.vehicle_types_url
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error fetching vehicle types: {e}")
            return None
        
    def _fetch_system_alerts(self):
        url = self.settings.system_alerts_url
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error fetching system alerts: {e}")
            return None
        
    def _fetch_station_information(self):
        url = self.settings.station_info_url
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error fetching station information: {e}")
            return None

    def _fetch_station_status(self):
        url = self.settings.station_status_url
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error fetching station status: {e}")
            return None

    def fetch(self):
        data = {
            "vehicle_types": self._fetch_vehicle_types(),
            "system_alerts": self._fetch_system_alerts(),
            "station_information": self._fetch_station_information(),
            "station_status": self._fetch_station_status()
        }
        return data

# Example usage
if __name__ == "__main__":
    bixi = Bixi()
    data = bixi.fetch()
    print(data)