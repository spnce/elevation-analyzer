from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Iterable, List
from .station import Station
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
        print(f"Report written to {filename}")


def _filter_stations(stations: Iterable[Station], state: str) -> List[Station]:
    return [station for station in stations if station.state.upper() == state.upper()]


def build_report(stations: Iterable[Station], state: str) -> StationReport:
    state_specific = _filter_stations(stations, state)

    if len(state_specific) == 0:
        raise ValueError(f"No stations found in {state}")

    elevations = [station.elev for station in state_specific if station.elev is not None]
    median_elevation = median(elevations)
    max_elevation = max(elevations)
    min_elevation = min(elevations)

    return StationReport(
        state=state.upper(),
        station_count=len(state_specific),
        maximum_elevation=max_elevation,
        minimum_elevation=min_elevation,
        average_elevation=mean(elevations),
        median_elevation=median_elevation,
        highest_stations=[station for station in state_specific if station.elev == max_elevation],
        lowest_stations=[station for station in state_specific if station.elev == min_elevation],
        median_stations = [station for station in state_specific if station.elev == median_elevation],
    )
