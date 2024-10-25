from dataclasses import dataclass
from Entities.entity import Entity


@dataclass
class Transaction(Entity):
    idCar: str
    idClient:str
    sumParts: int
    sumLabor: int
    date: str
    hours: str