from rental.core.database import JsonDatabase
from rental.model.user import User


class UserService(object):
    @classmethod
    def add_user(cls, name, year, license, phone):
        user = User(name=name, year=year, license=license, phone=phone)
        db = JsonDatabase.get_instance()
        db.persist('user', user.uuid, user)
        db.flush()
        return user

    @classmethod
    def get_user_list(cls):
        users = []
        records = JsonDatabase.get_instance().fetch_all('user')
        for k, v in records.items():
            users.append(User(**v))
        return users
