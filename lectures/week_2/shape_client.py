"""some client code to use
subclasses of Shape
"""


# demonstrate code that uses Shape
# without knowing whether it is Square or Triangle
from shape import Shape
from point import Point
from typing import List


def shape_place(shape_list: List[Shape]):
    """
    Moves, draws, and prints areas of Shapes in shape_list.
    """
    for s in shape_list:
        for p in [Point(100, 0), Point(100, 200), Point(-200, -100)]:
            s.move_by(p)
            s.draw()
            # this line is fine, even though Shape.get_area is not
            # implemented
            print(s.get_area())
            # the line below would get flagged for no attribute x
            # print(s.x)


if __name__ == '__main__':
    # code that uses shape_place with specific Shapes
    from square import Square
    from right_angle_triangle import RightAngleTriangle
    L = [Square([Point(0, 0), Point(40, 0), Point(40, 40), Point(0, 40)]),
         RightAngleTriangle([Point(-100, 0), Point(0, 0), Point(-100, 50)])]
    shape_place(L)
    from time import sleep
    sleep(5)
