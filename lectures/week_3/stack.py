""" implement stack ADT
"""
from container import Container, EmptyContainerException


class Stack(Container):
    """ Last-in, first-out (LIFO) stack.
    """

    def __init__(self):
        """ Create a new, empty Stack self.

        >>> s = Stack()
        """
        self._key = -1
        self._storage = {}

    def add(self, obj) -> None:
        """ Add object obj to top of Stack self.

        >>> s = Stack()
        >>> s.add(3)
        """
        self._key += 1
        self._storage[self._key] = obj

    def remove(self) -> object:
        """
        Remove and return top element of Stack self.

        Assume Stack self is not empty, otherwise
        raises EmptyStackException
        >>> s = Stack()
        >>> s.add(5)
        >>> s.add(7)
        >>> s.remove()
        7
        """
        if self.is_empty():
            raise EmptyContainerException("cannot remove from empty Stack")
        else:
            self._key -= 1
            return self._storage.pop(self._key + 1)

    def is_empty(self) -> bool:
        """
        Return whether Stack self is empty.

        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.add(s)
        >>> s.is_empty()
        False
        """
        return len(self._storage) == 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
