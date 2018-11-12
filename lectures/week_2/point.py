"""
point module
"""
from typing import Any


class Point:
    """ Represent a two-dimensional points

    x - horizontal position
    y - vertical position
    """
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        """ Initialize a new points
        """

        self.x, self.y = x, y

    def __eq__(self, other: Any) -> bool:
        """ Return whether self is equivalent to other.

        >>> Point(3, 5) == Point(3.0, 5.0)
        True
        >>> Point(3, 5) == Point(5, 3)
        False
        >>> Point(3, 5) == 7
        False
        """

        return (type(self) == type(other)
                and self.x == other.x
                and self.y == other.y)

    def __str__(self) -> str:
        """ Return a string representation of self

        >>> print(Point(3, 5))
        (3.0, 5.0)
        """

        return '({}, {})'.format(float(self.x), float(self.y))

    def distance_from_origin(self) -> float:
        """ Return the distance from the origin of this points

        >>> Point(3, 4).distance_from_origin()
        5.0
        """

        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance_to(self):
        pass

    def __add__(self, other: 'Point'):
        pass

if __name__ == "__main__":
    from doctest import testmod
    testmod()

    p = Point(3, 4)
