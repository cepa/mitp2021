import os
import json
from rental.core import settings


class JsonDatabase(object):
    __instance = None
    __path = None
    __database = {}

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
            cls.__path = '%s/database.json' % settings.ROOT_PATH
            cls.__instance.load()
        return cls.__instance

    def dump(self):
        print(self.__database)

    def load(self):
        if os.path.exists(self.__path):
            with open(self.__path, 'r') as fd:
                self.__database = json.load(fd)

    def flush(self):
        with open(self.__path, 'w') as fd:
            json.dump(self.__database, fd)
