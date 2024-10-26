from Entities.transactionValidator import TranzactieValidator
from Entities.carValidation import CarValidation
from Entities.clientCardValidation import ClientValidator
from Repository.repository import Repository
from Entities.transaction import Transaction


class TransactionService:
    def __init__(self, repositoryTransaction: Repository, tansVali: TranzactieValidator,
                 carVali: CarValidation, cltCardVali: ClientValidator,
                 repositoryCar: Repository, repositoryCardClient: Repository):
        self.__repository = repositoryTransaction
        self.__tansVali = tansVali
        self.__carVali = carVali
        self.__cltCardVali = cltCardVali
        self.__repositoryCar = repositoryCar
        self.__repositoryCardClient = repositoryCardClient

    def getAll(self):
        return self.__repository.read()

    def add(self, id, idCar, idClient, sumParts, sumLabor, date, hour):
        if self.__repositoryCar.read(idCar) is None:
            raise KeyError(f'Car {idCar} does not exist')

        trans = Transaction(id, idCar, idClient, sumParts, sumLabor, date, hour)

        self.__tansVali.valideaza(trans)

        # parts are free if the car is under guarantee
        car = self.__repositoryCar.read(idCar)
        if car.guarantee == "DA":
            trans.sumParts = 0

        # apply discount if an card client exists

        if idClient is not None:
            self.__repositoryCardClient.read(idClient)  # bcs maybe it's not null but it's not a valid card either

            trans.sumLabor = sumLabor - (sumLabor * 10 / 100)

        self.__repository.add(trans)

    def remove(self, id):
        car = self.__repository.read(id)

        self.__repository.remove(id)

    def update(self, id, idCar, idClient, sumParts, sumLabor, date, hour):
        if self.__repositoryCar.read(idCar) is None:
            raise KeyError(f'Car {idCar} does not exist')

        if self.__repositoryCardClient.read(idClient) is None:
            raise KeyError(f'Client {idClient} does not exist')

        trans = Transaction(id, idCar, idClient, sumParts, sumLabor, date, hour)

        self.__tansVali.valideaza(trans)

        # parts are free for cars under g
        car = self.__repositoryCar.read(idCar)
        if car.guarantee == "DA":
            trans.sumParts = 0

        # apply discount
        if idClient is not None:
            self.__repositoryCardClient.read(idClient)

            trans.sumLabor = sumLabor - (sumLabor * 10 / 100)

        self.__repository.update(trans)

    def cascade_delete(self, car_id):
        cascade = []

        for transaction in self.__repository.read():
            if transaction.idCar == car_id:
                cascade.append(transaction)
                self.__repository.remove(transaction.idEntity)

        car = self.__repositoryCar.read(car_id)
        cascade.append(car)
        self.__repositoryCar.remove(car.idEntity)

    def removeFromStartToEnd(self, a1, b1):
        a = a1.split('.')
        b = b1.split('.')
        lista = []
        tranzactii = self.getAll()
        for tranzactie in tranzactii:
            tran = tranzactie.data.split('.')
            if a[2] < tran[2] < b[2]:
                self.remove(tranzactie.idEntitate)
                lista.append(tranzactie)
            elif a[2] == tran[2] == b[2] \
                    and a[1] < tran[1] < b[1]:
                self.remove(tranzactie.idEntitate)
                lista.append(tranzactie)
            elif a[2] == tran[2] == b[2] \
                    and a[1] == tran[1] == b[1] \
                    and a[0] < tran[0] < b[0]:
                self.remove(tranzactie.idEntitate)
                lista.append(tranzactie)
