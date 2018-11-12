
from typing import Callable, Union
from time import time
from matplotlib import pyplot as plt
import timeit


def f1(n: int)->int:
    n = 17 * n**(1/2)
    n = n + 3

    if n > 97:
        return n
    else:
        return n // 2


def f2(n: int)->int:
    sum_t = 0
    for ii in range(n):
        sum_t += ii
    return sum_t


def f3(n: int)->int:
    i, sum_t = 0, 0
    while i ** 2 < n:
        j = 0
        while j ** 2 < n:
            sum_t += i * j
            j += 1
        i += 1
    return sum_t


def bubblesort(n: int) -> list:
    """
    Sort the items in list_ in non-decreasing order.

    """
    list_=range(n)
    j = len(list_) - 1
    while j != 0:
        # Swap every item that is out of order.
        for i in range(j):
            if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
        j -= 1
    return list_

def f4(n:int)->list:
    list_ = list(range(n))
    return list_.append(list_[len(list_) - 1] + 1)

def f5(n:int)->None:
    list_ = list(range(n))
    return len(list_)


def f6(n:int)->int:
    sum = 0
    for i in range(n // 2):
        sum += i * n
    return sum

def f7(n:int)->int:
    sum,i = 0, n
    while i > 1:
        sum += i * n
        i = i // 2
    return sum


def f8(n:int)->int:
    sum = 0
    for i in range(n // 2):
        for j in range(n**2):
            sum += (i + j) * n
    return sum

def f9(n:int)->int:
    sum = 0
    if n % 2 == 0:
        for i in range(n * n):
            sum += 1
    else:
        for i in range(n + 100):
            sum += i
    return sum


def plot(results:list)->None:
    x = [i[0] for i in results]
    y = [i[1] for i in results]
    plt.plot(x,y)
    plt.show()

def test(f:Callable[[list],Union[int, None]], n:list)->tuple:
    # start = time()
    # f(n)
    # taken = time() - start
    taken = timeit.timeit('{}({})'.format(f.__name__,n), number=10, globals=globals())
    return n, taken

if __name__ == '__main__':
    results =[]
    inputs = [100, 1000, 10000, 100000, 1000000]

    #inputs = range(100000, 200000)

    for i in inputs:
        results.append(test(f1, i))
    plot(results)

