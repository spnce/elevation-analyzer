from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from station import Station

@dataclass_json
@dataclass
class StationReport:
    state: str
    station_count: int
    maximum_elevation: float
    minimum_elevation: float
    average_elevation: float
    median_elevation: float

    highest_stations: List[Station]
    lowest_stations: List[Station]
    median_stations: List[Station]