"""
client code for container
"""
from container import Container


def container_cycle(c: Container, i: int) -> None:
    """ Cycle i items through Container c.

    """
    for n in range(i):
        c.add(n)
    while not c.is_empty():
        print(c.remove())


if __name__ == "__main__":
    # now it's 2027
    from stack import Stack
    from sack import Sack
    from queue1 import Queue
    L = [Stack(), Sack(), Queue()]
    for s in L:
        print("\nCycling through {}".format(s))
        container_cycle(s, 10)
