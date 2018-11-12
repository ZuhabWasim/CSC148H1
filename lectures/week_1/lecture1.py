from typing import List

""" Notes
-'is' looks at ID
-'==' looks at value
-'*' looks at type
-'[:1] looks at mutability
-you can annotated/provide a type contract for attributes of a class
-python first creates a blank object then secondly initializes
-in python you import type Any to make sure that there is no error if you compare it to another type
-(returns false in that case)
-self is already defined as type (innate) class
-a, b = 5, 3 is tuple unpacking and python creates a tuple and assigns the tupple (a, b) (5, 3)
DONT DO THIS
For an object, you can alter and add attributes to the Class that shouldn't be there
in the console.
i.e. Turtle.neck = 'Wrinkly'
python says 
"Does this class already have the local attribute neck? Then it looks into the blueprints to see
what can be done." Python adds the neck attribute 
"""


def repeated(st: str, n: int) -> List[str]:
    """ Return a list of words n times.

    >>> repeated('a', 2)
    ['a', 'a']
    >>> repeated('a', 0)
    []
    >>> repeated('', 2)
    ['', '']
    """

    return [st] * n


# WHAT NOT TO DO
"""
from turtle import Turtle

t = Turtle()
t.pos()
t.forward()
t.left()
"""

"""
# How to wrongly define classes
class Point:
    pass #Pass holds the code at the points, literally for nothing


>>> p = Point()
>>> p
<Point object at 0x7f123871927>
>>> p.x = 3
>>> p.x
3
>>> p.y = 4
>>> Point.x = 3

#giving every points an x value is too time consuming so we create a function to do so
#not that this function is not a class method, but in the main program
>>> def init(points, x, y): 
        points.x, points.y = x, y

>>> init(p, 5, 12)
>>> p.x
5
>>> p.y
12

>>> Point.__init__ = init

>>> p2 = Point(3, 4)
>>> p2.x
3
>>> p2.y
4
#note that this Point class only has two parameters but the init function has 3 parameters
#this is because the class's own type is implicity defined from saying Point(,)

>>> def distance_to_zero(points):
        return (points.x**2 + points.y**2)**0.5

>>> p.x
5
>>> p.y
12
>>> distance_to_zero(p)
13.0
>>> Point.distance_to_origin = distance_to_zero
#note that the no paranthesis says that this is an attribute rather than method, the first method
#exists inside Point while the other one exists in the main module
#the information of distance_origin is implicit now so no need to put in arguments below

>>> p.distance_to_origin() #no parameters because you only pass in one argument
# if you passed in an argument you would get an error because the implicit arguments counts as one which
# makes you pass two arguments instead of one

#methods in classes are really just functions that have their first paramater as the class's type
#and it is redundant to ever pass in that parameter
"""

"""Defining Point the right way"""
