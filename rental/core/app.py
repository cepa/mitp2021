from rental.core.database import JsonDatabase


class Application(object):

    def run(self):
        print('Wypozyczalnia v1.0')
        db = JsonDatabase.get_instance()
        db.dump()
        print(db.exists('car', 123))
        db.persist('car', 123, 'du du dupa')
        db.dump()
        db.flush()
