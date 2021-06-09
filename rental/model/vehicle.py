from . import Model
from .entity import EntityMixin


class Vehicle(EntityMixin, Model):
    def __init__(self, **kwargs):
        self.make = None
        self.model = None
        self.wheels = None
        self.year = None
        super().__init__(**kwargs)


class Car(Vehicle):
    def __init__(self, **kwargs):
        self.displacement = None
        self.door = None
        self.seats = None
        super().__init__(**kwargs)


class Motorcycle(Vehicle):
    def __init__(self, **kwargs):
        self.displacement = None
        self.type = None
        super().__init__(**kwargs)


class Bicycle(Vehicle):
    def __init__(self, **kwargs):
        self.frame = None
        super().__init__(**kwargs)
