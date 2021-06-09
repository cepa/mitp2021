import os
import json
from rental.core import settings
from rental.core.object import JsonEncoder


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
            json.dump(self.__database, fd, cls=JsonEncoder)

    def exists(self, type, key):
        return True if type in self.__database and str(key) in self.__database[type] else False

    def persist(self, type, key, object):
        if type not in self.__database:
            self.__database[type] = {}
        self.__database[type][str(key)] = object

    def fetch(self, type, key):
        return self.__database[type][str(key)] if type in self.__database and str(key) is self.__database[type] else None

    def fetch_all(self, type):
        return self.__database[type] if type in self.__database else []

    def remove(self, type, key):
        if type in self.__database and str(key) in self.__database[type]:
            del self.__database[type][key]

    def remove_all(self, type):
        if type in self.__database:
            del self.__database[type]
