from Entities.entity import Entity
from Repository.repository import Repository


class RepositoryInMemory(Repository):
    def __init__(self):
        self.entities = {}

    def read(self, idEntity=None):
        if idEntity is None:
            return list(self.entities.values())
        if idEntity in self.entities:
            return self.entities[idEntity]
        else:
            return None

    def add(self, entity: Entity):
        if self.read(entity.idEntity) is not None:
            raise KeyError("Entity already exists")
        self.entities[entity.idEntity] = entity

    def remove(self, idEntity):
        if self.read(idEntity) is None:
            raise KeyError("Entity not found")
        del self.entities[idEntity]

    def update(self, entity: Entity):
        if self.read(entity.idEntity) is None:
            raise KeyError("Entity not found")

        self.entities[entity.idEntity].update(entity)
