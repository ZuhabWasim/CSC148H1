""" implement sack ADT
"""
from random import randint


class Sack:
    """ Last-in, first-out (LIFO) sack.
    """

    def __init__(self) -> None:
        """ Create a new, empty Sack self.

        >>> s = Sack()
        """
        self._contains = []

    def add(self, obj: object) -> None:
        """ Add object obj to top of Sack self.

        >>> s = Sack()
        >>> s.add(5)
        """
        self._contains.append(obj)

    def remove(self) -> object:
        """
        Remove and return top element of Sack self.

        Assume Sack self is not emp.
        """
        return self._contains.pop(randint(0, len(self._contains) - 1))

    def is_empty(self) -> bool:
        """
        Return whether Sack self is empty.

        >>> s = Sack()
        >>> s.is_empty()
        True
        >>> s.add(5)
        >>> s.is_empty()
        False
        """
        return len(self._contains) == 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    s = Sack()
    for i in range(20):
        s.add(i)
    while not s.is_empty():
        print(s.remove())
