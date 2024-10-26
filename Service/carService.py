from Entities.car import Car
from Entities.carValidation import CarValidation
from Repository.repository import Repository

class CarService:
    def __init__(self, repository: Repository, carvali: CarValidation):
        self.__carrepository = repository
        self.__carValidation = carvali

    def getCars(self):
        return self.__carrepository.read()

    def addCar(self, idCar, model, year, milage, guarantee):
        car = Car(idCar, model, year, milage, guarantee)

        self.__carValidation.validateCar(car)
        self.__carrepository.add(car)

    def removeCar(self, idCar):
        car = self.__carrepository.read(idCar)

        self.__carrepository.remove(idCar)

    def updateCar(self, idCar, model, year, milage, guarantee):
        car = Car(idCar, model, year, milage, guarantee)
        self.__carValidation.validateCar(car)
        self.__carrepository.update(car)
