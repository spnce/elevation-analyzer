from dataclasses import dataclass

@dataclass
class Station:
    uid: int
    state: str
    name: str
    ll: str
    elev: float