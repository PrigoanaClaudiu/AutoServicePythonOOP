import jsonpickle

from Entities.entity import Entity
from Repository.repositoryInMemory import RepositoryInMemory


class RepositoryJson(RepositoryInMemory):
    def __init__(self):
        super().__init__()
        self.filename = 'repository.json'

    def __readfile(self):
        pass

    def __writefile(self):
        pass

    def read(self, idEntity=None):
        pass

    def add(self, entity: Entity):
        pass

    def remove(self, idEntity):
        pass

    def update(self, entity: Entity):
        pass
