from Entities.entity import Entity
from Repository.repository import Repository


class RepositoryInMemory(Repository):
    def __init__(self):
        self.entities = {}

    def read(self, idEntity=None):
        pass

    def add(self, entity: Entity):
        pass

    def remove(self, idEntity):
        pass

    def update(self, entity: Entity):
        pass
