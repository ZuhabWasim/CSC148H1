"""
code for RightAngleTriangle class
"""
from shape import Shape
from point import Point
from typing import List
from time import sleep


class RightAngleTriangle(Shape):
    """
    A right-angle-triangle Shape.
    """

    def __init__(self, corners: List[Point]) -> None:
        """
        Create RightAngleTriangle self with vertices corners.

        Extends Shape.__init__

        Assume corners[0] is the 90 degree angle.

        >>> s = RightAngleTriangle([Point(0, 0), Point(1, 0), Point(0, 2)])
        >>> print(s)
        RightAngleTriangle([(0.0, 0.0), (1.0, 0.0), (0.0, 2.0)])
        """
        Shape.__init__(self, corners)

    def get_area(self) -> float:
        """
        Return RightAngleTriangle self's area.

        Overrides Shape.get_area

        >>> s = RightAngleTriangle([Point(0,0), Point(10,0), Point(0,20)])
        >>> s.get_area()
        100.0
        """
        leg1 = self.corners[-1].distance_to(self.corners[0])
        leg2 = self.corners[0].distance_to(self.corners[1])
        return (leg1 * leg2) / 2.0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    rat = RightAngleTriangle([Point(0, 0), Point(100, 0), Point(0, 300)])
    rat.draw()
    rat.move_by(Point(50, 100))
    rat.draw()
    sleep(5)
    print(rat.get_area())
    print(rat)
