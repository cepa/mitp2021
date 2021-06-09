class Repository(object):
    @classmethod
    def exists(cls, key):
        """
        Find if an entity exists.
        Returns:
            - True of False
        """
        raise NotImplementedError()

    @classmethod
    def get(cls, key):
        """
        Get entity by key.
        Returns: Entity object if one is found by key.
        Raises: NotFoundError is entity isn't found.
        """
        raise NotImplementedError()

    @classmethod
    def save(cls, entity):
        """
        Save entity in the repository.
        """
        raise NotImplementedError()

    @classmethod
    def delete(cls, entity):
        """
        Delete entity from the repository.
        """
        raise NotImplementedError()

    @classmethod
    def query(cls, offset=None, limit=None, sort=None, filter=None, **kwargs):
        """
        Query repository to find entities.
        """
        raise NotImplementedError()

    @classmethod
    def count(cls, filter=None, **kwargs):
        """
        Return number of entities in the repository.
        """
        raise NotImplementedError()

    @classmethod
    def purge(cls, filter=None, **kwargs):
        """
        Remove all entities from the repository.
        """
        raise NotImplementedError()
