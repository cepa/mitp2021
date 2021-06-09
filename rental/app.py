from rental.service.user import UserService
from rental.service.car import CarService


MAIN_MENU = '''
Akcje:
    1  - Dodaj uzytkownika do bazy
    2  - Dodaj samochod do bazy
    11 - Lista uzytkownikow
    12 - Lista samochodow
    99 - Wyjscie
'''

class Application(object):
    def action_add_user(self):
        print('Wypelnij dane aby dodac uzytkownika: ')
        user = UserService.add_user(
            name=input('Nazwa uzytkownika: '),
            year=input('Rok urodzeniaL: '),
            license=input('Rodzaj prawajazdy [A, B, AB]: '),
            phone=input('Telefon: ')
        )
        user.summary()

    def action_show_user_list(self):
        users = UserService.get_user_list()
        for user in users:
            user.summary()

    def action_add_car(self):
        print('Wypelnij dane aby dodac samochod: ')
        car = CarService.add_car(
            make=input('Marka: '),
            model=input('Model: '),
            wheels=input('Liczba kol: '),
            year=input('Rok produkcji: '),
            displacement=input('Pojemnosc: '),
            door=input('Liczba drzwi: '),
            seats=input('Liczba siedzen: ')
        )
        car.summary()

    def action_show_car_list(self):
        cars = CarService.get_car_list()
        for car in cars:
            car.summary()

    def main_loop(self):
        try:
            print(MAIN_MENU)

            actions = {
                '1': lambda: self.action_add_user(),
                '2': lambda: self.action_add_car(),
                '11': lambda: self.action_show_user_list(),
                '12': lambda: self.action_show_car_list(),
            }

            choice = input('Wpisz numer: ')
            if choice in actions:
                actions[choice]()
            elif choice == '99':
                return False
            else:
                print('\nNie ma takiej akcji, sprobuj ponownie.')
                return True

        except ValueError as err:
            print("Uwaga blad danych: {}".format(err))
            return True
        except RuntimeError as err:
            print("Uwaga blad: {}".format(err))
            return True

    def run(self):
        print('Wypozyczalnia v1.0')
        while self.main_loop():
            pass
