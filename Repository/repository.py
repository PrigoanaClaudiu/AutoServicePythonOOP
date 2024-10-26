from typing import Protocol
from Entities.entity import Entity

class Repository(Protocol):
    def read(self, idEntity=None):
        ...

    def add(self, entity: Entity):
        ...

    def remove(self, idEntity):
        ...

    def update(self, entity: Entity):
        ...