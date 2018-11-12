""" Lecture 6 Notes

when you define a function, you create an object called function and you can use this to call itself
through definition time it can call a function that doesn't exist, but it is legal to define it that way
as the error only occurs in run time.

def f(n):
    return 2 * g(n)
# definition exists and is created in memory but causes an error if run,
# but if we define g = len (an already existing object) the f(n) will work.

>>> def f(n):
... return g(n) + 1
...
>>> f(2) # CRASH!
>>> def g(n):
...     return 2 * n
...
>>> f(2)

To understand recursion, trace from simple to complex:
    I trace sum_list(17)
    I trace sum_list([1, 2, 3]). Remember how the built-in
    sum works...
    I trace sum_list([1, [2, 3], 4, [5, 6]]). Immediately
    replace calls you've already traced (or traced something
    equivalent) by their value
    I trace sum_list([1, [2, [3 ,4], 5], 6 [7, 8]]).
    Immediately replace calls you've already traced by their
    value.

L = [1, 2, 3]
L.append(L)
L
[1, 2, 3, [...]]
L[3]
[1, 2, 4, [...]]


"""
from typing import List


def sum_list(lst: List[int]):
    """
    Return the sum of all ints in L.
    >>> sum_list([1, [2, 3], [4, 5, [6, 7], 8]])
    36
    >>> sum([])
    0
    """
    if isinstance(lst, list):
        return sum([sum_list(x) for x in lst])
    else:
        return lst
