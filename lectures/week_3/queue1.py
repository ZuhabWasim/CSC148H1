"""
queue implementation
"""


class Queue:
    """
    A first-in, first-out (FIFO) queue.
    """

    def __init__(self) -> None:
        """
        Create and initialize new Queue self.

        >>> q = Queue()
        """
        self.contents = []

    def add(self, obj: object) -> None:
        """
        Add object at the back of Queue self.

        >>> q = Queue()
        >>> q.add(7)
        """
        self.contents.append(obj)

    def remove(self) -> object:
        """
        Remove and return front object from Queue self.

        Queue self must not be empty.

        >>> q = Queue()
        >>> q.add(3)
        >>> q.add(5)
        >>> q.remove()
        3
        """
        if not self.is_empty():
            return self.contents.pop(0)

    def __str__(self) -> str:
        """

        :return:
        :rtype:
        """
        st = '['

        while not self.is_empty():
            st += "'" + str(self.remove()) + "', "

        st = st[0:-2] + "]"
        return st

    def is_empty(self) -> bool:
        """
        Return whether Queue self is empty

        >>> q = Queue()
        >>> q.add(5)
        >>> q.is_empty()
        False
        >>> q.remove()
        5
        >>> q.is_empty()
        True
        """
        return len(self.contents) == 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    q1 = Queue()
    q1.add('Q')
    q1.add('Y')

    q2 = Queue()
    q2.add('W')

    q3 = Queue()
    q3.add('A')
    q3.add('E')

    q1.add(q3.remove())
    q1.add(q2.remove())

    q2.add(q1.remove())

    q3.add(q1.remove())
    q3.add(q1.remove())
    q3.add(q1.remove())
    q3.add(q2.remove())

    print(q1, q2, q3)
