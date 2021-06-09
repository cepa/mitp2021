from . import Model
from .entity import EntityMixin


class User(EntityMixin, Model):
    def __init__(self, **kwargs):
        self.name = None
        self.date_of_birth = None
        self.driving_license = None
        self.phone_number = None
        super().__init__(**kwargs)
