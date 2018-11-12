"""
experiment with recursion and memoization
"""
# some recursive explorations

from random import shuffle


def fibonacci(n):
    """
    Return the nth fibonacci number, that is n if n < 2,
    or fibonacci(n-2) + fibonacci(n-1) otherwise.
    @param int n: a non-negative integer
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(3)
    """
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fib_memo(n, seen):
    """
    Return the nth fibonacci number reasonably quickly.
    @param int n: index of fibonacci number
    @param dict[int, int] seen: already-seen results
    """
    if n not in seen:
        seen[n] = (n if n < 2
                    else fib_memo(n - 2, seen) + fib_memo(n - 1 , seen))
    return seen[n]


def qs(list_):
    """
    Return a new list consisting of the elements of list_ in
    ascending order.
    @param list list_: list of comparables
    @rtype: list
    >>> qs([1, 5, 3, 2])
    [1, 2, 3, 5]
    """
    if len(list_) < 2:
        return list_[:]
    else:
        return (qs([i for i in list_ if i < list_[0]])
                + [list_[0]]
                + qs([i for i in list_[1:] if i >= list_[0]]))

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    from time import time

    start = time()
    res = fibonacci(34)
    print("Fib took {}, result = {}".format(time() - start, res))

    start = time()
    res = fib_memo(34, seen=dict())
    print("Fib took {}, result = {}".format(time() - start, res))