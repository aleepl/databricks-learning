import logging

from ingestion.bixi.services.station_information import StationInfoService
from ingestion.bixi.services.station_status import StationStatusService
from ingestion.bixi.services.system_alerts import SystemAlertsService
from ingestion.bixi.services.vehicle_types import VehicleTypesService
from ingestion.bixi.settings import BixiSettings

logger = logging.getLogger(__name__)


def etl() -> None:
    logger.info("Starting ETL ingestion process for Bixi data.")

    # Settings and params
    settings = BixiSettings()
    bucket_name = settings.s3_bucket_name

    # Create service instances
    station_info_service = StationInfoService(settings)
    station_status_service = StationStatusService(settings)
    system_alerts_service = SystemAlertsService(settings)
    vehicle_types_service = VehicleTypesService(settings)

    # Fetch data
    station_info_data = station_info_service.fetch()
    station_status_data = station_status_service.fetch()
    system_alerts_data = system_alerts_service.fetch()
    vehicle_types_data = vehicle_types_service.fetch()

    # Load data to S3
    station_info_service.load(bucket_name, station_info_data)
    station_status_service.load(bucket_name, station_status_data)
    system_alerts_service.load(bucket_name, system_alerts_data)
    vehicle_types_service.load(bucket_name, vehicle_types_data)

    logger.info("Ending ETL ingestion process for Bixi data.")


if __name__ == "__main__":
    etl()
