class AttrMixin(object):
    def __getattr__(self, k):
        try:
            return self[k]
        except KeyError:
            raise KeyError("%s: Missing key '%s'" % (self.__class__.__name__, k))

    def __setattr__(self, k, v):
        self[k] = v


class SerializableMixin(object):
    def serialize(self, include=None, exclude=None, override=None):
        state = self.__getstate__()
        serialized = state.copy()

        if include is not None and isinstance(include, list):
            for k in state:
                if k not in include:
                    del serialized[k]

        if exclude is not None and isinstance(exclude, list):
            for k in exclude:
                if k in state:
                    del serialized[k]

        if override is not None and isinstance(override, dict):
            for k,v in override.items():
                serialized[k] = v

        return serialized

    @classmethod
    def unserialize(cls, data):
        obj = cls()
        if data is not None:
            if not isinstance(data, dict):
                raise ValueError("%s: Can't unserialize data" % cls.__name__)
            obj.__setstate__(data)
        return obj

    @classmethod
    def new(cls, data=None):
        return cls.unserialize(data)


class PatchableMixin(object):
    def patch(self, state=None, **kwargs):
        self.update({k: state[k] for k in state.keys() if state[k] is not None})


# This class represents an object with flexible parameters, you can expand object properties like a dictionary.
class FlexibleObject(dict, AttrMixin, SerializableMixin):
    def __init__(self, **kwargs):
        self.__setstate__(kwargs)

    def __getstate__(self):
        return {k: v for k, v in self.items()}

    def __setstate__(self, state):
        self.update({k: self.__duct_tape__(state[k]) for k in state})

    def __duct_tape__(self, thing):
        if isinstance(thing, FlexibleObject):
            return thing
        if isinstance(thing, dict):
            return FlexibleObject(**thing)
        if isinstance(thing, (list, tuple)):
            return [self.__duct_tape__(item) for item in thing]
        return thing


# This class represents an object with strict parameters, you can only set or get parameters that are pre defined.
class StrictObject(FlexibleObject, PatchableMixin):
    def update(self, state=None, **kwargs):
        if state:
            super().update(**{k: self.__duct_tape__(state[k]) for k in set(state.keys()).intersection(self.keys())})
        super().update(**{k: self.__duct_tape__(kwargs[k]) for k in set(kwargs.keys()).intersection(self.keys())})
