""" implement class Shape
"""
from point import Point
from turtle import Turtle
from typing import List, Any


class Shape:
    """
    A Shape that can draw itself, move, and
    report area..

    corners - corners that define this Shape
    """
    corners: List[Point]

    def __init__(self, corners: List[Point]) -> None:
        """
        Create a new Shape self with defined by its corners.

        >>> s = Shape([Point(0, 0), Point(1, 0), Point(1, 1)])
        >>> s.corners
        [Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)]
        """
        # shallow copy of corners
        self.corners = corners[:]
        # private turtle
        self._turtle = Turtle()

    def __eq__(self, other: Any) -> bool:
        """
        Return whether Shape self is equivalent to other.

        >>> s1 = Shape([Point(0, 0), Point(1, 0), Point(1, 1)])
        >>> s2 = Shape([Point(0, 0), Point(1, 0), Point(1, 1)])
        >>> s3 = Shape([Point(0, 0), Point(1, 0), Point(1, 2)])
        >>> s1 == s2
        True
        >>> s1 == s3
        False
        """
        return type(self) == type(other) and self.corners == other.corners

    def __str__(self) -> str:
        """
        Return an informative string about self.

        >>> print(Shape([Point(0, 0), Point(1, 0), Point(0, 1)]))
        Shape([(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)])
        """
        corners_string = ", ".join([str(c) for c in self.corners])
        # classes have a __name__ string
        return type(self).__name__ + "([{}])".format(corners_string)

    def __repr__(self) -> str:
        """
        Return a string that would evaluate to a Shape equivalent to self.

        >>> Shape([Point(0, 0), Point(1, 0), Point(0, 1)])
        Shape([Point(0.0, 0.0), Point(1.0, 0.0), Point(0.0, 1.0)])
        """
        # classes have a __name__ string
        return type(self).__name__ + "({})".format(self.corners)

    def get_area(self) -> float:
        """
        Return the area of Shape self.
        """
        raise NotImplementedError("must implement a subclass!")

    def move_by(self, offset_point) -> None:
        """
        Move Shape self to a new position by adding
        Point offset_point to each corner.

        >>> s = Shape([Point(0, 0), Point(1, 0), Point(0, 1)])
        >>> s.move_by(Point(1, 1))
        >>> print(s)
        Shape([(1.0, 1.0), (2.0, 1.0), (1.0, 2.0)])
        """
        # list comprehension,
        # see lab2, bottom of page 1
        self.corners = [(c + offset_point) for c in self.corners]
        # equivalent to...
        # new_corners = []
        #  for c in self.corners:
        #     new_corners.append(c.add(offset_point))
        # self.corners = new_corners

    def draw(self) -> None:
        """
        Draw Shape self.
        """
        self._turtle.penup()
        self._turtle.goto(self.corners[-1].x, self.corners[-1].y)
        self._turtle.pendown()
        for i in range(len(self.corners)):
            self._turtle.goto(self.corners[i].x, self.corners[i].y)
        self._turtle.penup()
        self._turtle.goto(0, 0)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
