from rental.core.database import JsonDatabase
from rental.model.vehicle import Car


class CarService(object):
    @classmethod
    def add_car(cls, make, model, wheels, year, displacement, door, seats):
        db = JsonDatabase.get_instance()
        car = Car(uuid=db.next_id(),
                  make=make,
                  model=model,
                  wheels=wheels,
                  year=year,
                  displacement=displacement,
                  door=door,
                  seats=seats)
        db.persist('car', car.uuid, car)
        db.flush()
        return car

    @classmethod
    def get_car(cls, car_id):
        record = JsonDatabase.get_instance().fetch('car', car_id)
        if record is None:
            raise RuntimeError("Nie znaleziono auta od ID=%s" % car_id)
        return Car(**record)

    @classmethod
    def get_car_list(cls):
        cars = []
        records = JsonDatabase.get_instance().fetch_all('car')
        for k, v in records.items():
            cars.append(Car(**v))
        return cars
