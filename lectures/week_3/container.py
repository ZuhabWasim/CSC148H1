""" implement Container
"""


class EmptyContainerException(Exception):
    """
    Exceptions called when empty Container used inappropriately
    """
    pass


class Container:
    """ Container with add, remove, and is_empty methods.

    This is an abstract class that is not meant to be instantiated itself,
    but rather subclasses are to be instantiated.
    """

    def __init__(self) -> None:
        """
        Create a new Container self.
        """
        self._contents = None
        raise NotImplementedError("Override this!")

    def add(self, obj) -> None:
        """
        Add obj to Container self.
        """
        raise NotImplementedError("Override this!")

    def remove(self) -> object:
        """
        Remove and return an object from Container self.

        Assume that Container self is empty.
        """
        raise NotImplementedError("Override this!")

    def is_empty(self) -> bool:
        """
        Return whether Container self is empty.
        """
        raise NotImplementedError("Override this!")
