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

    def cautareFullText(self, para):
        cars = self.__carrepository.read()
        rez = []
        for i in cars:
            if para in i.model or para in str(i.year) \
                    or para in str(i.milage) \
                    or para in ("DA" if i.guarantee else "NU"):
                rez.append(i)
        return rez

    def updateGuarentee(self):
        for car in self.getCars():
            if int(car.year) >= 2018 and int(car.mileage) <= 60000:
                self.updateCar(car.idEntity,
                               car.model,
                               car.year,
                               car.mileage, 'DA')
            else:
                self.updateCar(car.idEntity,
                               car.model,
                               car.year,
                               car.mileage, 'NU')
