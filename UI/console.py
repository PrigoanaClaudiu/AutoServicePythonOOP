from Repository.repositoryJson import RepositoryJson
from Service.carService import CarService
from Service.transactionService import TransactionService
from Service.clientCardService import ClientCardService


class Console:
    def __init__(self, car_service: CarService, transaction_service: TransactionService,
                 client_card_service: ClientCardService):
        self.__car_service = car_service
        self.__transaction_service = transaction_service
        self.__client_card_service = client_card_service

    def run_menu(self):
        while True:
            print("1. Car CRUD.")
            print("2. Client Card CRUD.")
            print("3. Transaction CRUD.")
            print("4. Functionalities.")
            print("5. Generate random clients.")
            print("6. Cascade delete.")
            print("x. Exit.")
            option = input("Choose an option: ")

            if option == '1':
                self.run_car_crud_menu()
            elif option == '2':
                self.run_client_card_crud_menu()
            elif option == '3':
                self.run_transaction_crud_menu()
            elif option == '4':
                self.run_functionalities()
            elif option == '5':
                self.generate_random_clients()
            elif option == '6':
                car_id = input("Enter the ID of the car to be deleted: ")
                self.__transaction_service.cascade_delete(car_id)
            elif option == 'x':
                break
            else:
                print("Invalid option! Please reload:")

    def run_car_crud_menu(self):
        while True:
            print("1. Add car.")
            print("2. Delete car.")
            print("3. Update car.")
            print("a. Show all cars.")
            print("x. Exit.")
            option = input("Choose an option: ")

            if option == '1':
                self.ui_add_car()
            elif option == '2':
                self.ui_delete_car()
            elif option == '3':
                self.ui_update_car()
            elif option == 'a':
                self.show_all_cars()
            elif option == 'x':
                break
            else:
                print("Wrong option, please try again!")

    def ui_add_car(self):
        try:
            car_id = input("Enter car ID: ")
            model = input("Enter model: ")
            purchase_year = input("Enter purchase year: ")
            km_number = input("Enter the number of kilometers: ")
            in_warranty = input("Warranty? (DA/NU): ")
            self.__car_service.addCar(car_id, model, purchase_year, km_number, in_warranty)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def ui_delete_car(self):
        try:
            car_id = input("Enter the ID of the car to be deleted: ")
            self.__car_service.removeCar(car_id)
        except KeyError as e:
            print(e)

    def ui_update_car(self):
        try:
            car_id = input("Enter the ID of the car to be updated: ")
            model = input("Enter the new model: ")
            purchase_year = input("Enter the purchase year: ")
            km_number = input("Enter the new number of kilometers: ")
            in_warranty = input("Is it under warranty? (yes or no): ")
            self.__car_service.updateCar(car_id, model, purchase_year, km_number, in_warranty)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def show_all_cars(self):
        for car in self.__car_service.getCars():
            print(car)

    def run_client_card_crud_menu(self):
        while True:
            print("1. Add client card.")
            print("2. Delete client card.")
            print("3. Update client card.")
            print("a. Show all clients.")
            print("x. Exit.")
            option = input("Choose an option: ")

            if option == '1':
                self.ui_add_client()
            elif option == '2':
                self.ui_delete_client()
            elif option == '3':
                self.ui_update_client()
            elif option == 'a':
                self.show_all_clients()
            elif option == 'x':
                break
            else:
                print("Wrong option, please try again!")

    def ui_add_client(self):
        try:
            client_id = input("Enter client ID: ")
            last_name = input("Enter last name: ")
            first_name = input("Enter first name: ")
            ssn = input("Enter CNP: ")
            birth_date = input("Enter birth date: ")
            registration_date = input("Enter registration date: ")
            self.__client_card_service.verifyCNP(last_name, first_name, ssn, birth_date, registration_date)
            self.__client_card_service.addClientCard(client_id, last_name, first_name, ssn, birth_date, registration_date)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def ui_delete_client(self):
        try:
            client_id = input("Enter client ID: ")
            self.__client_card_service.removeClientCard(client_id)
        except KeyError as e:
            print(e)

    def ui_update_client(self):
        try:
            client_id = input("Enter client ID: ")
            last_name = input("Enter last name: ")
            first_name = input("Enter first name: ")
            ssn = input("Enter CNP: ")
            birth_date = input("Enter birth date: ")
            registration_date = input("Enter registration date: ")
            self.__client_card_service.verifyCNP(last_name, first_name, ssn, birth_date, registration_date)
            self.__client_card_service.updateClientCard(client_id, last_name, first_name, ssn, birth_date, registration_date)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def show_all_clients(self):
        for client in self.__client_card_service.getClientCard():
            print(client)


    def run_transaction_crud_menu(self):
        while True:
            print("1. Add transaction.")
            print("2. Delete transaction.")
            print("3. Update transaction.")
            print("a. Show all transactions.")
            print("x. Exit.")
            option = input("Choose an option: ")

            if option == '1':
                self.ui_add_transaction()
            elif option == '2':
                self.ui_delete_transaction()
            elif option == '3':
                self.ui_update_transaction()
            elif option == 'a':
                self.show_all_transactions()
            elif option == 'x':
                break
            else:
                print("Wrong option, please try again!")

    def ui_add_transaction(self):
        try:
            transaction_id = input("Enter transaction ID: ")
            car_id = input("Enter car ID: ")
            client_id = input("Enter client ID: ")
            parts_cost = float(input("Enter parts cost: "))
            labor_cost = float(input("Enter labor cost: "))
            date = input("Enter date: ")
            hour = input("Enter hour: ")
            self.__transaction_service.add(transaction_id, car_id, client_id, parts_cost, labor_cost, date, hour)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

    def ui_delete_transaction(self):
        try:
            transaction_id = input("Enter transaction ID: ")
            self.__transaction_service.remove(transaction_id)
        except KeyError as e:
            print(e)
        except Exception as e:
            print(e)

    def ui_update_transaction(self):
        try:
            transaction_id = input("Enter the transaction ID to be updated: ")
            car_id = input("Enter car ID: ")
            client_id = input("Enter client ID: ")
            parts_cost = float(input("Enter parts cost: "))
            labor_cost = float(input("Enter labor cost: "))
            date = input("Enter date: ")
            hour = input("Enter hour: ")
            self.__transaction_service.update(transaction_id, car_id, client_id, parts_cost, labor_cost, date, hour)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

    def show_all_transactions(self):
        result = []
        for transaction in self.__transaction_service.getAll():
            total_cost = transaction.sumLabor + transaction.sumParts
            result.append({
                "transaction": transaction,
                "total cost": total_cost,
            })
        print(result)

    def run_functionalities(self):
        while True:
            print("1. Full-text search for cars.")
            print("2. Full-text search for clients.")
            print("3. Show all transactions within a given amount range.")
            print("4. Show cars sorted descending by labor cost.")
            print("5. Show client cards sorted descending by discount value.")
            print("6. Delete all transactions within a certain date range.")
            print("7. Update warranty status for each car: a car is under warranty if and only if it is less than 3 years old and has less than 60,000 km.")
            print("x. Exit.")

            option = input("Choose an option: ")
            if option == "1":
                param = input("Enter search parameter: ")
                self.ui_full_text_search_cars(param)
            elif option == "2":
                param = input("Enter search parameter: ")
                self.ui_full_text_search_clients(param)
            elif option == "3":
                low = float(input("Enter lower bound of the range: "))
                high = float(input("Enter upper bound of the range: "))
                self.ui_show_transactions_in_amount_range(low, high)
            elif option == "4":
                self.ui_show_cars_sorted_by_labor_cost()
            elif option == "5":
                self.ui_show_clients_sorted_by_discount()
            elif option == "6":
                start = input("Enter start date: ")
                end = input("Enter end date: ")
                self.ui_delete_transactions_in_date_range(start, end)
            elif option == "7":
                self.ui_update_car_warranty_status()
            elif option == "x":
                break
            else:
                print("Wrong option! Please reload:")

    # Define functionality methods here...
    def generate_random_clients(self):
        while True:
            print("1. Generate n random clients")
            print("x. Iesire.")
            optiune = input("Optiune: ")
            if optiune == "1":
                n = int(input("n: "))
                self.__client_card_service.clientiGenerati(n)
                self.show_all_clients()
            elif optiune == "x":
                break
            else:
                print("Optiune invalida. Reincercati.")