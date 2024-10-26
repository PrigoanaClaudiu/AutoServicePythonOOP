import jsonpickle

from Entities.entity import Entity
from Repository.repositoryInMemory import RepositoryInMemory


class RepositoryJson(RepositoryInMemory):
    def __init__(self):
        super().__init__()
        self.filename = 'repository.json'

    def __readfile(self):
        try:
            with open(self.filename, 'r') as f:
                return jsonpickle.loads(f.read())
        except Exception as e:
            return e

    def __writefile(self):
        with open(self.filename, 'w') as f:
            f.write(jsonpickle.dumps(self.__readfile()))

    def read(self, idEntity=None):
        pass

    def add(self, entity: Entity):
        self.entities = self.__readfile()
        super().add(entity)
        self.__writefile()

    def remove(self, idEntity):
        self.entities = self.__readfile()
        super().remove(idEntity)
        self.__writefile()

    def update(self, entity: Entity):
        self.entities = self.__readfile()
        super().update(entity)
        self.__writefile()
