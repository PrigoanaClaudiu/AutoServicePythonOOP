from Entities.car import Car


# class CarValidation: == class CarValidation(): -> no inheritance from a superclass, just from object
# class CarValidation(Entity): -> inheritance from a superclass Entity
class CarValidation:
    def validateCar(self, masinuta: Car):
        erori = []
        if int(masinuta.year) < 0:
            erori.append("Anul achizitiei trebuie sa fie mai mare ca 0.")
        if int(masinuta.mileage) < 0:
            erori.append(("Nr de kilometrii trebuie sa fie mai mari ca 0."))
        m = ['DA', 'NU']
        if masinuta.guarantee not in m:
            erori.append("Garantie poate lua valorile DA/NU")
        if len(erori) > 0:
            raise ValueError(erori)

    def garan(self, masinuta: Car):
        '''verifica daca masina este sau nu in garantie'''
        m = ['DA', 'NU']
        if masinuta.guarantee in m:
            if masinuta.guarantee == 'da':
                return True
        return False
