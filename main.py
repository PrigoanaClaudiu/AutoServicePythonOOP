from Entities.carValidation import CarValidation
from Entities.clientCardValidation import ClientValidator
from Entities.transactionValidator import TranzactieValidator
from Repository.repositoryJson import RepositoryJson
from Service.transactionService import TransactionService
from Service.clientCardService import ClientCardService
from Service.carService import CarService
from UI.console import Console

def main():
    carRepositoryJson = RepositoryJson("cars.json")
    carValidator = CarValidation()
    carService = CarService(carRepositoryJson, carValidator)

    clientCardRepositoryJson = RepositoryJson("clients card.json")
    clientCardValidator = ClientValidator()
    clientCardService = ClientCardService(clientCardRepositoryJson, clientCardValidator)

    transactionRepositoryJson = RepositoryJson("transactions.json")
    transactionValidator = TranzactieValidator()
    transactionService = TransactionService(transactionRepositoryJson, transactionValidator,
                                            carValidator, clientCardValidator,
                                            carRepositoryJson, clientCardRepositoryJson)

    console = Console(carService, transactionService, clientCardService)

    console.run_menu()

main()