"""
subclass Square of Shape
"""
from shape import Shape
from point import Point
from typing import List
from time import sleep


class Square(Shape):
    """
    A Square; extends Shape
    """

    def __init__(self, corners: List[Point]) -> None:
        """
        Create Square self with corners.

        Assume all sides are equal and corners are square.

        Extends Shape (adds to documentation!).

        >>> s = Square([Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)])
        >>> print(s)
        Square([(0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)])
        """
        Shape.__init__(self, corners)

    def get_area(self) -> float:
        """
        Return area of this square.

        over-rides Shape._get_area()

        >>> s = Square([Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)])
        >>> s.get_area()
        1.0
        """
        return self.corners[0].distance_to(self.corners[1]) ** 2


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    s = Square([Point(0, 0), Point(100, 0), Point(100, 100), Point(0, 100)])
    s.draw()
    s.move_by(Point(100, 200))
    s.draw()
    sleep(5)
    print(s.get_area())
