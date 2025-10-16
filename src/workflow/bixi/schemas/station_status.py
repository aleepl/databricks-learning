from pyspark.sql.types import (
    StructType, StructField, StringType, IntegerType, LongType, BooleanType, ArrayType
)

vehicle_type_available_schema = StructType([
    StructField("vehicle_type_id", StringType(), False),
    StructField("count", IntegerType(), False),
])

station_status_schema = StructType([
    StructField("station_id", StringType(), False),
    StructField("num_bikes_available", IntegerType(), False),
    StructField("num_ebikes_available", IntegerType(), False),
    StructField("vehicle_types_available", ArrayType(vehicle_type_available_schema), False),
    StructField("num_bikes_disabled", IntegerType(), False),
    StructField("num_docks_available", IntegerType(), False),
    StructField("num_docks_disabled", IntegerType(), False),
    StructField("is_installed", IntegerType(), False),
    StructField("is_renting", IntegerType(), False),
    StructField("is_returning", IntegerType(), False),
    StructField("last_reported", LongType(), False),
    StructField("eightd_has_available_keys", BooleanType(), False),
    StructField("is_charging", BooleanType(), False),
])

station_status_payload_schema = StructType([
    StructField("last_updated", LongType(), False),
    StructField("ttl", IntegerType(), False),
    StructField("version", StringType(), False),
    StructField("data", StructType([
        StructField("stations", ArrayType(station_status_schema), False)
    ]), False),
])