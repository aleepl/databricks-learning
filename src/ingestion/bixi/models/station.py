from dataclasses import dataclass

@dataclass
class Station:
    station_id: str
    external_id: str
    name: str
    short_name: str
    lat: float
    lon: float
    rental_methods: List[str]
    capacity: int
    electric_bike_surcharge_waiver: bool
    is_charging: bool
    eightd_has_key_dispenser: bool
    has_kiosk: bool