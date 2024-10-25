from dataclasses import dataclass
from Entities.entity import Entity


@dataclass
class Car(Entity):
    model: str
    year: int
    mileage: float
    guarantee: str
