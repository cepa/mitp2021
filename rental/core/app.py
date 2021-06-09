from rental.core.database import JsonDatabase


class Application(object):

    def run(self):
        print('Wypozyczalnia v1.0')
        db = JsonDatabase.get_instance()
        db.dump()
        db.flush()
