from rental.service.user import UserService
from rental.service.car import CarService
from rental.service.rental import RentalService


MAIN_MENU = '''
Akcje:
    1  - Dodaj uzytkownika do bazy
    2  - Dodaj samochod do bazy
    5  - Wynajmij pojazd
    11 - Lista uzytkownikow
    12 - Lista samochodow
    13 - Lista wynajmowanych pojazdow
    23 - Usun wynajem
    99 - Wyjscie
'''

class Application(object):
    def action_add_user(self):
        print('Wypelnij dane aby dodac uzytkownika')
        user = UserService.add_user(
            name=input('Nazwa uzytkownika: '),
            year=input('Rok urodzeniaL: '),
            license=input('Rodzaj prawajazdy [A, B, AB]: '),
            phone=input('Telefon: ')
        )
        user.summary()

    def action_show_user_list(self):
        print('Lista uzytkownikow')
        users = UserService.get_user_list()
        for user in users:
            user.summary()

    def action_add_car(self):
        print('Wypelnij dane aby dodac samochod')
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
        print('Lista samochodow')
        cars = CarService.get_car_list()
        for car in cars:
            car.summary()

    def action_rent_vehicle(self):
        print('Wynajmij pojazd')
        type = input('Typ pojazdu (auto, moto, rower): ')
        if 'auto' in type:
            vehicle = CarService.get_car(input('ID pojazdu: '))
        else:
            raise ValueError("Zly typ pojazdu: %s" % type)
        user = UserService.get_user(input('ID uzytkownika: '))
        rental = RentalService.rent_vehicle(type, user, vehicle, None, None)
        rental.summary()

    def action_show_rental_list(self):
        print('Lista wynajmowanych pojazdow')
        rentals = RentalService.get_rental_list()
        for rental in rentals:
            rental.summary()

    def action_remove_rental(self):
        print('Usun wynajem')
        RentalService.remove_rental(input('ID wynajmu do usuniecia: '))

    def main_loop(self):
        try:
            print(MAIN_MENU)

            actions = {
                '1': lambda: self.action_add_user(),
                '2': lambda: self.action_add_car(),
                '5': lambda: self.action_rent_vehicle(),
                '11': lambda: self.action_show_user_list(),
                '12': lambda: self.action_show_car_list(),
                '13': lambda: self.action_show_rental_list(),
                '23': lambda: self.action_remove_rental(),
            }

            choice = input('Wpisz numer akcji: ')
            if choice in actions:
                print('')
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
