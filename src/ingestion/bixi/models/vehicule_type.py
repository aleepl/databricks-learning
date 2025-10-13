from dataclasses import dataclass


@dataclass
class VehiculeType:
    vehicle_type_id: str
    form_factor: str
    propulsion_type: str
    max_range_meters: int
