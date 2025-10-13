from pydantic_settings import BaseSettings


class BixiSettings(BaseSettings):
    # Source URLs
    vehicle_types_url: str = "https://gbfs.velobixi.com/gbfs/2-2/en/vehicle_types.json"
    system_alerts_url: str = "https://gbfs.velobixi.com/gbfs/2-2/en/system_alerts.json"
    station_info_url: str = "https://gbfs.velobixi.com/gbfs/2-2/en/station_information.json"
    station_status_url: str = "https://gbfs.velobixi.com/gbfs/2-2/en/station_status.json"

    # S3 Bucket
    s3_bucket_name: str = "databricks-playground-bucket-20251003"

    class Config:
        env_file = ".env"
