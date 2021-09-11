from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from dataclass_csv import DataclassReader
from io import TextIOWrapper
from typing import Iterable


@dataclass_json
@dataclass
class Station:
    uid: int
    state: str
    name: str
    ll: str = field(default="Unknown")
    elev: float = field(default=None)


def as_stations(file_contents: TextIOWrapper) -> Iterable[Station]:
    return DataclassReader(file_contents, Station)
