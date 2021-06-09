from . import Model
from .entity import EntityMixin


class User(EntityMixin, Model):
    def __init__(self, **kwargs):
        self.name = None
        self.year = None
        self.license = None
        self.phone = None
        super().__init__(**kwargs)
