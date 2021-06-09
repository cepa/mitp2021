from rental.core.database import JsonDatabase
from rental.service.user import UserService


class Application(object):

    def run(self):
        print('Wypozyczalnia v1.0')
        user = UserService.add_user('Lukasz Cepowski', 1988, 'AB', '123456678')
        user.summary()
        JsonDatabase.get_instance().flush()
