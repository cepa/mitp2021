from rental.service.user import UserService


MAIN_MENU = '''
Akcje:
    1 - Dodaj uzytkownika do bazy
    9 - Lista uzytkownikow
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

    def main_loop(self):
        try:
            print(MAIN_MENU)

            actions = {
                '1': lambda: self.action_add_user(),
                '9': lambda: self.action_show_user_list(),
            }

            choice = input('Wpisz numer: ')
            if choice in actions:
                actions[choice]()
            else:
                print('\nNie ma takiej akcji, sprobuj ponownie.')
                return True

        except ValueError as err:
            print("Uwaga blad danych: {}".format(err))
            return True
        except RuntimeError as err:
            print("Uwaga blad: {}".format(err))
            return True
        return False if 'tak' in input('\nWpisz tak jezeli chcesz wyjsc z programu: ') else True

    def run(self):
        print('Wypozyczalnia v1.0')
        while self.main_loop():
            pass
