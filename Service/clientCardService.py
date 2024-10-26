from random import randint, choice

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

    def clientiGenerati(self, n):
        nrClienti = 0
        numeC = ['Pop', 'Prigoana', 'Marginean', 'Lupas', 'Pasca', 'Nemes']
        prenumeC = ['Claudiu', 'Alex', 'Adi', 'Razvan', 'Denis', 'Marius']
        dataNas = ['16.01.2003', '17.01.1993', '20.08.1994', '09.08.1999']
        dataInr = ['18.01.2019', '19.09.2020', '21.09.2021', '23.08.2021']

        while nrClienti < n:
            idClient = str(randint(1, 100000))
            if self.__repository.read(idClient) is None:  # Verifică dacă ID-ul este unic înainte de a continua
                nume = choice(numeC)
                prenume = choice(prenumeC)
                cnp = str(randint(1000000000000, 9999999999999))
                dataN = choice(dataNas)
                dataI = choice(dataInr)
                client = ClientCard(idClient, nume, prenume, cnp, dataN, dataI)

                self.__repository.add(client)
                nrClienti += 1

    def cautareFullText(self, para):
        clienti = self.__repository.read()
        rez = []
        for i in clienti:
            if para in i.name or para in i.surname \
                    or para in i.CNP or para in i.date_of_birth \
                    or para in i.date_of_registration:
                rez.append(i)
        return rez
