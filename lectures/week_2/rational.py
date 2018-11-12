"""
module for rational stuff...
"""
from typing import Any


class Rational:
    """
    A rational number

    num - numerator
    denom - denominator; must be non-zero
    """
    num: int
    denom: int

    def __init__(self, num: int, denom: int) -> None:
        """
        Create new Rational self with numerator num and
        denominator denom --- denom must not be 0.

        >>> Rational(1, 2).num
        1
        >>> Rational(3, 4).denom
        4
        """
        self.num, self.denom = num, denom
        self._invariant()

    def __eq__(self, other: Any) -> bool:
        """
        Return whether Rational self is equivalent to other.

        >>> r1 = Rational(3, 5)
        >>> r2 = Rational(6, 10)
        >>> r3 = Rational(4, 7)
        >>> r1 == r2
        True
        >>> r1.__eq__(r3)
        False
        >>> r1 == "3/5"
        False
        """
        self._invariant()
        return (type(self) == type(other)
                and (self.num * other.denom == other.num * self.denom))

    def __str__(self) -> str:
        """
        Return a user-friendly string representation of
        Rational self.

        >>> print(Rational(3, 5))
        3/5
        """
        self._invariant()
        #other._invariant()
        return "{}/{}".format(self.num, self.denom)

    def __repr__(self) -> str:
        """
        Return a string representation that would evaluate to an equivalent
        Rational to self.

        >>> Rational(3, 4).__repr__()
        'Rational(3, 4)'
        """
        self._invariant()
        #other._invariant()
        return "Rational({}, {})".format(self.num, self.denom)

    def __lt__(self, other: "Rational") -> bool:
        """
        Return whether Rational self is less than other.

        >>> Rational(3, 5).__lt__(Rational(4, 7))
        False
        >>> Rational(3, 5).__lt__(Rational(5, 7))
        True
        >>> Rational(1, 2) < Rational(1, -4)
        False
        """
        self._invariant()
        other._invariant()
        return (self.num * other.denom < self.denom * other.num
                if self.denom * other.denom > 0
                else self.num * other.denom > self.denom * other.num)

    def __mul__(self, other: "Rational") -> "Rational":
        """
        Return the product of Rational self and Rational other.

        >>> print(Rational(3, 5).__mul__(Rational(4, 7)))
        12/35
        """
        self._invariant()
        other._invariant()
        return Rational(self.num * other.num, self.denom * other.denom)

    def _invariant(self) -> None:
        # quit if self.denom is 0
        # Exercise: make this return informative string
        assert self.denom != 0, "Zero self.denom!: {}/{}".format(self.num,
                                                                 self.denom)

    def __add__(self, other: "Rational") -> "Rational":
        """
        Return the sum of Rational self and Rational other.

        >>> print(Rational(3, 5).__add__(Rational(4, 7)))
        41/35
        """
        self._invariant()
        other._invariant()
        return Rational(self.num * other.denom + self.denom * other.num,
                        self.denom * other.denom)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # r1 = Rational(3, 5)
    # r2 = Rational(4, 7)
    # r1 < r2
    # r1.__add__(r2)
    # r1.__mul__(r2)
    # r1 == r2
    # r1 == "three-fifths"
