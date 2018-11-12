"""
rational module
"""
from typing import Any

class Rational:
    """ Representation of a rational number.

    p - numerator
    q - denominator
    """

    p: int
    q: int
    decimal: float

    def __init__(self, p: int, q: int):
        """ Initializes the rational.
        """

        self.p = p
        self.q = q
        self.decimal = p / q

    def __str__(self) -> str:
        """ Gives a string representation of the rational.

        >>> print(Rational(3, 5))
        3 / 5 = 0.6
        """

        return '{} / {} = {}'.format(self.p, self.q, self.p / self.q)

    def __eq__(self, other: Any) -> bool:
        """ Returns if two rationals are the same.

        >>> Rational(3, 5) == Rational(15, 25)
        True
        >>> Rational(3, 5) == Rational(3, 4)
        False
        >>> Rational(3, 5) == 5
        False
        """

        return (type(self) == type(other)
                and self.p * other.q == self.q * other.p)

if __name__ == "__main__":
    from doctest import testmod
    testmod()
