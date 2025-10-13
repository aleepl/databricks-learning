from dataclasses import dataclass
from typing import List


@dataclass
class TimeRange:
    start: int
    end: int


@dataclass
class SystemAlerts:
    alert_id: str
    type: str
    times: List[TimeRange]
    url: str
    summary: str
    description: str
    last_updated: int
