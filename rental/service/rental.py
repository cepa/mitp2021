from rental.core.database import JsonDatabase
from rental.model.rental import Rental


class RentalService(object):
    @classmethod
    def rent_vehicle(cls, type, user, vehicle, begin_time, finish_time):
        db = JsonDatabase.get_instance()
        rental = Rental(uuid=db.next_id(),
                        type=type,
                        user=user,
                        vehicle=vehicle,
                        begin_time=begin_time,
                        finish_time=finish_time)
        db.persist('rental', rental.uuid, rental)
        db.flush()
        return rental

    @classmethod
    def get_rental(cls, rental_id):
        record = JsonDatabase.get_instance().fetch('rental', rental_id)
        if record is None:
            raise RuntimeError("Nie znaleziono wynajmu od ID=%s" % rental_id)
        return Rental(**record)

    @classmethod
    def get_rental_list(cls):
        rentals = []
        records = JsonDatabase.get_instance().fetch_all('rental')
        for k, v in records.items():
            rentals.append(Rental(**v))
        return rentals

    @classmethod
    def remove_rental(cls, rental_id):
        db = JsonDatabase.get_instance()
        db.remove('rental', rental_id)
        db.flush()
