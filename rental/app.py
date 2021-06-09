from rental.model.vehicle import Car


class Application(object):

    def run(self):
        print('Wypozyczalnia v1.0')
        Car().summary()
