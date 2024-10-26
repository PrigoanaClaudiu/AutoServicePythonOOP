import jsonpickle

from Entities.entity import Entity
from Repository.repositoryInMemory import RepositoryInMemory


class RepositoryJson(RepositoryInMemory):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def __readfile(self):
        try:
            with open(self.filename, 'r') as f:
                return jsonpickle.loads(f.read())
        # if the file is empty or contains invalid details, i will return an empty dict
        except Exception as e:
            return {}

    def __writefile(self):
        with open(self.filename, 'w') as f:
            f.write(jsonpickle.dumps(self.entities, indent=2))

    def read(self, idEntity=None):
        self.entities = self.__readfile()
        return super().read(idEntity)

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
