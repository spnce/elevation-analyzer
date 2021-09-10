from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Station:
    uid: int
    state: str
    name: str
    ll: str = field(default="Unknown")
    elev: float = field(default=None)