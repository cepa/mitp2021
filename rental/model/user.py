from . import Model
from .entity import EntityMixin


class User(EntityMixin, Model):
    def __init__(self, **kwargs):
        self.name = None
        self.year = None
        self.license = None
        self.phone = None
        super().__init__(**kwargs)

    def summary(self):
        print('\t%s, %s, %s, %s' % (self.name, self.year, self.license, self.phone))
