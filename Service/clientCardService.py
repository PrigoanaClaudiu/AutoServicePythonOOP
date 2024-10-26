from Entities.clientCard import ClientCard
from Repository.repository import Repository
from Entities.clientCardValidation import ClientValidator


class ClientCardService:
    def __init__(self, repositoryCard: Repository, clientVali: ClientValidator):
        self.__clientValidator = clientVali
        self.__repository = repositoryCard

    def getClientCard(self):
        return self.__repository.read()

    def addClientCard(self, idClient, name, surname, CNP, date_of_birth, date_of_registration):
        card = ClientCard(idClient, name, surname, CNP, date_of_birth, date_of_registration)

        self.__clientValidator.valideaza(card)
        self.__repository.add(card)

    def removeClientCard(self, idClient):
        client = self.__repository.read(idClient)

        self.__repository.remove(idClient)

    def updateClientCard(self, idClient, name, surname, CNP, date_of_birth, date_of_registration):
        client = ClientCard(idClient, name, surname, CNP, date_of_birth, date_of_registration)

        self.__clientValidator.valideaza(client)
        self.__repository.update(client)

    def verifyCNP(self, name, surname, CNP, date_of_birth, date_of_registration):
        if not all([name, surname, CNP, date_of_birth, date_of_registration]):
            raise IndexError

        if CNP in [client.CNP for client in self.__repository.read()]:
            print("CNP already exists!")
