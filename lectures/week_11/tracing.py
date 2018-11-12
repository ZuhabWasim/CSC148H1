"""
some examples for tracing code
"""
from typing import Union, Callable


def f(n: int) -> int:
    """
    Return g(n + 1)
    """
    x = 1
    x = g(n + 1)
    return x


def g(n: int) -> int:
    """
    Return h(n + 1)
    """
    x = 2
    x = h(n + 1)
    return x


def h(n: int) -> int:
    """ return n + 1
    """
    x = n + 1
    return x


def sum_list(list_: Union[list, int]) -> int:
    """
    Return list_, if it is an int, or the sum of all elements
    of list_ and its sublists.
    """
    if not isinstance(list_, list):
        return list_
    else:
        flat_list = [sum_list(x) for x in list_]
        return sum(flat_list)


class Parent:
    """
    Parent class...
    """
    def f(self, n: int) -> int:
        """
        Return 2 * g(n)
        """
        return 2 * self.g(n)

    def g(self, n) -> int:
        """
        Return 3 * n
        """
        return 3 * n


class Child(Parent):
    """
    Child class...
    """
    def g(self, n: int) -> int:
        """
        Return n

        Overrides Parent.g
        """
        return n


def filter_list(list_: list, predicate: Callable[[object], bool]) -> None:
    """
    Modify list_ so that it contains only elements that satisfy predicate.
    """
    temp_list = []
    while len(list_) > 0:
        if predicate(list_[0]):
            temp_list.append(list_.pop(0))
        else:
            scrap = list_.pop(0)
    list_ = temp_list
    print(list_)

if __name__ == "__main__":
    list_ = [98, 99, 100]
    print(sum_list([1, 2, [3, 4, 5], 6]))

    """
    n = 217
    c = Child()
    print(c.f(1))
    """
