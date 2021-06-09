from rental.core.database import JsonDatabase
from rental.model.user import User


class UserService(object):
    @classmethod
    def add_user(cls, name, year, license, phone):
        db = JsonDatabase.get_instance()
        user = User(uuid=db.next_id(),
                    name=name,
                    year=year,
                    license=license,
                    phone=phone)
        db.persist('user', user.uuid, user)
        db.flush()
        return user

    @classmethod
    def get_user(cls, user_id):
        record = JsonDatabase.get_instance().fetch('user', user_id)
        if record is None:
            raise RuntimeError("Nie znaleziono uzytkownika od ID=%s" % user_id)
        return User(**record)

    @classmethod
    def get_user_list(cls):
        users = []
        records = JsonDatabase.get_instance().fetch_all('user')
        for k, v in records.items():
            users.append(User(**v))
        return users
