from dataclasses import dataclass
from typing import List


@dataclass
class VehiculeTypeAvailable:
    vehicle_type_id: str
    count: int


@dataclass
class StationStatus:
    station_id: str
    num_bikes_available: int
    num_ebikes_available: int
    vehicle_types_available: List[VehiculeTypeAvailable]
    num_bikes_disabled: int
    num_docks_available: int
    num_docks_disabled: int
    is_installed: int
    is_renting: int
    is_returning: int
    last_reported: int
    eightd_has_available_keys: bool
    is_charging: bool
