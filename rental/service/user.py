from rental.core.database import JsonDatabase
from rental.model.user import User


class UserService(object):
    @classmethod
    def add_user(cls, name, year, license, phone):
        user = User(name=name, year=year, license=license, phone=phone)
        JsonDatabase.get_instance().persist('user', user.uuid, user)
        return user
