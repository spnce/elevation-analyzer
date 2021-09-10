from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Station:
    uid: int
    state: str
    name: str
    ll: str
    elev: float