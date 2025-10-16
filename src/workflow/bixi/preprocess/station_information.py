import logging
from typing import List


from ingestion.bixi.models.station import Station
from pyspark.sql.functions import current_timestamp
from pyspark.sql import DataFrame

logger = logging.getLogger(__name__)


class StationInfoResponse:
    last_updated: int
    ttl: int
    version: str
    data: List[Station]

class StationInfoService:
    def __init__(self, spark) -> None:
        self._spark = spark

    def preprocess(self, df_raw: DataFrame) -> None:
        if not df_raw or df_raw.rdd.isEmpty():
            logger.warning("No station data to preprocess; skipping.")
            return

        logger.info("Preprocessing station information data.")
        # Add ingestion timestamp
        df = df_raw.withColumn("processed_at", current_timestamp())

        # Show schema and sample data for debugging

        return df