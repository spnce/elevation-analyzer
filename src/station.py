from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from dataclass_csv import DataclassReader
from io import TextIOWrapper
from typing import Iterable


@dataclass_json
@dataclass
class Station:
    """
    A Station represents the physical location of a climate station.
    Its schema can be used for serialzing & deserializing csv & json.

    Attributes:
        uid (int): The station's unique identifier.
        state (str): The state where the station is located.
        name (str): A descriptive name of the station.
        ll (str): The station's latitude & longitude. Ex: "[42, -120]"
        elev (float): The elevation of the station.
    """
    uid: int
    state: str
    name: str
    ll: str = field(default="Unknown")
    elev: float = field(default=None)


def as_stations(file_contents: TextIOWrapper) -> Iterable[Station]:
    """Apply the Station schema to a CSV input"""
    return DataclassReader(file_contents, Station)
