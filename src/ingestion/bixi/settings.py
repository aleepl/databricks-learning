from pydantic_settings import BaseSettings


class BixiSettings(BaseSettings):
    vehicle_types_url: str = "https://gbfs.velobixi.com/gbfs/2-2/en/vehicle_types.json"
    system_alerts_url: str = "https://gbfs.velobixi.com/gbfs/2-2/en/system_alerts.json"
    station_info_url: str = "https://gbfs.velobixi.com/gbfs/2-2/en/station_information.json"
    station_status_url: str = "https://gbfs.velobixi.com/gbfs/2-2/en/station_status.json"

    class Config:
        env_file = ".env"
