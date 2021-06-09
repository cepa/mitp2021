from rental.core.database import JsonDatabase
from rental.model.vehicle import Car


class CarService(object):
    @classmethod
    def add_car(cls, make, model, wheels, year, displacement, door, seats):
        car = Car(make=make,
                  model=model,
                  wheels=wheels,
                  year=year,
                  displacement=displacement,
                  door=door,
                  seats=seats)

        db = JsonDatabase.get_instance()
        db.persist('car', car.uuid, car)
        db.flush()
        return car

    @classmethod
    def get_car_list(cls):
        cars = []
        records = JsonDatabase.get_instance().fetch_all('car')
        for k, v in records.items():
            cars.append(Car(**v))
        return cars
