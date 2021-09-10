from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List
from station import Station
from dataclass_csv import DataclassReader
from statistics import mean, median

OUTPUT_FMT = "elevation_report_{state}.json"
JSON_INDENTATION = 4

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

    def dump(self):
        filename = OUTPUT_FMT.format(state=self.state)
        with open(filename, mode='w') as out_file:
            out_file.write(self.to_json(indent=JSON_INDENTATION))


def _open_stations(stations_file: str, state: str) -> List[Station]:
    with open(stations_file) as stations:
        return [station for station in DataclassReader(stations, Station) if station.state == state]


def build_report(stations_file: str, state: str) -> StationReport:
    stations = _open_stations(stations_file, state)

    elevations = [station.elev for station in stations if station.elev is not None]
    median_elevation = median(elevations)
    max_elevation = max(elevations)
    min_elevation = min(elevations)

    return StationReport(
        state=state,
        station_count=len(stations),
        maximum_elevation=max_elevation,
        minimum_elevation=min_elevation,
        average_elevation=mean(elevations),
        median_elevation=median_elevation,
        highest_stations=[station for station in stations if station.elev == max_elevation],
        lowest_stations=[station for station in stations if station.elev == min_elevation],
        median_stations = [station for station in stations if station.elev == median_elevation],
    )
