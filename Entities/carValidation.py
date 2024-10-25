from Entities.car import Car


# class CarValidation: == class CarValidation(): -> no inheritance from a superclass, just from object
# class CarValidation(Entity): -> inheritance from a superclass Entity
class CarValidation:
    def validateCar(self, car: Car):
        if car.year <= 0:
            raise KeyError("The car's year must be greater than 0")
        if car.mileage <= 0:
            raise KeyError("The car's mileage must be greater than 0")
        if car.guarantee != "DA" or car.guarantee != "NU":
            raise KeyError("The car's guarantee must be DA or NU")
