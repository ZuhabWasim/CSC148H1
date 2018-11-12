""" implementation of class Sack
"""

from container import Container
from random import randint, shuffle


class Sack(Container):
    """ A Sack with elements in no particular order.
    """

    def __init__(self):
        """ Create a new, empty Sack self.

        @param Sack self: this Sack
        @rtype: None
        """
        # pairs as keys get put in a dict in
        # unpredictable order... unlike ints
        self._contents = []

    def add(self, obj):
        """ Add object obj to random position of Sack self.

        @param Sack self: this Sack
        @param object obj: object to place on Sack
        @rtype: None
        """
        self._contents.append(obj)
        shuffle(self._contents)  # randomizes the list

    def remove(self) -> object:
        """ Remove and return some random element of Sack self.

        Assume Sack self is not empty.

        @param Sack self: this Sack
        @rtype: object

        >>> s = Sack()
        >>> s.add(7)
        >>> s.remove()
        7
        """
        return self._contents.pop(randint(0, len(self._contents) - 1))

    def is_empty(self) -> bool:
        """ Return whether Sack self is empty.

        @param Sack self: this Sack
        @rtype: bool
        """
        return self._contents == []


if __name__ == "__main__":
    import doctest
    doctest.testmod()
