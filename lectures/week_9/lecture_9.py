""" notes
BST can only have
    - orderable data
    -
- sometimes problems are innately recursive, breaking the problem up into smaller problems

"""


def fibonacci(n: int) -> int:
    """
    Return the nth fibonacci number, that is n if n < 2,
    or fibonacci(n-2) + fibonacci(n-1) otherwise.
    """
    # return 1 if n == 0 or n == 1 else fibonacci(n - 2) - fibonacci(n - 1)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fib_mem(n: int, seen: dict) -> int:
    """ return nth fibonacci number *quickly*
    """
    if n not in seen:
        if n < 2:
            seen[n] = n
        else:
            seen[n] = fib_mem(n - 2, seen) + fib_mem(n - 1, seen)
    return seen[n]
