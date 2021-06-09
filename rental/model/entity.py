from uuid import uuid4, UUID


class EntityMixin(object):
    def __init__(self, **kwargs):
        if 'uuid' in kwargs:
            self.uuid = UUID(str(kwargs['uuid']))
            del kwargs['uuid']
        else:
            self.uuid = uuid4()
        super().__init__(**kwargs)
