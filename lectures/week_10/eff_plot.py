
from typing import Callable, Union
from time import time
from matplotlib import pyplot as plt


def f1(n: int)->None:
    n = 17 * n**(1/2)
    n = n + 3
    print("n is: {}.".format(n))
    if n > 97:
        print('big!')
    else:
        print('not so big!')


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


def test(f:Callable[[list],Union[int, None]], n:list)->tuple:
    start = time()
    f(n)
    taken = time() - start
    return n, taken


def plot(results:list)->None:
    x = [i[0] for i in results]
    y = [i[1] for i in results]
    plt.plot(x,y)
    plt.show()

if __name__ == '__main__':
    results =[]
    inputs = [1000, 10000, 100000, 1000000, 10000000]

    for i in inputs:
        results.append(test(f2, i))

    plot(results)