from pydantic import BaseModel


class Station(BaseModel):
    station_id: int
    external_id: str
    name: str
    short_name: str
    lat: float
    lon: float
    rental_methods: list[str]
    capacity: int
    electric_bike_surcharge_waiver: bool
    is_charging: bool
    eightd_has_key_dispenser: bool
    has_kiosk: bool


class StationStatus(BaseModel):
    station_id: int
    num_bikes_available: int
    num_ebikes_available: int
    vehicle_types_available: list[dict]
    num_bikes_disabled: int
    num_docks_available: int
    num_docks_disabled: int
    is_installed: int
    is_renting: int
    is_returning: int
    last_reported: int
    eightd_has_available_keys: bool
    is_charging: bool
