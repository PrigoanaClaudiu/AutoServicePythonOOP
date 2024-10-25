from dataclasses import dataclass
from abc import ABC

#dataclass simplifies the definiion of the class - automated constructor etc.
@dataclass
class Entity(ABC):
    idEntity: str
