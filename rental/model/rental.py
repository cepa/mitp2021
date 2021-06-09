from . import Model
from .entity import EntityMixin


class Rental(EntityMixin, Model):
    def __init__(self, **kwargs):
        self.type = None
        self.user = None
        self.vehicle = None
        self.begin_time = None
        self.finish_time = None
        super().__init__(**kwargs)

    def summary(self):
        print('ID: %s, Typ: %s, Uzytkownik (ID): %s, Pojazd (ID): %s, Od: %s, Do: %s' % (
            self.uuid, self.type, self.user.uuid, self.vehicle.uuid, self.begin_time, self.finish_time
        ))
