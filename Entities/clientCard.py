from dataclasses import dataclass
from Entities.entity import Entity


@dataclass
class ClientCard(Entity):
    name: str
    surname: str
    CNP: str
    date_of_birth: str
    date_of_registration: str
