"""class HashTable
"""
# import numpy as np
from time import time
# from matplotlib import pyplot as plt
from typing import Callable, Union


class HashTable:
    """
    A hash table for (key, value) 2-tuples

    === Attributes ===
    @param int capacity: total slots available
    @param list[list[tuple]] table: contents of table
    @param int collisions: number of collisions
    @param int items: number of items
    """

    items: int

    def __init__(self, capacity=2):
        """
        Create a hash table with capacity slots

        @param HashTable self: this hash table
        @param int capacity: number of slots in this table
        @rtype: None
        """
        self.capacity, self.collisions, self.items = capacity, 0, 0
        self.table = [[] for _ in range(self.capacity)]

    def __contains__(self, key):
        """ Return whether HashTable self contains key"

        @param HashTable self: this hash table
        @param object key: key to search for
        @rtype: bool
        """

    def __setitem__(self, key: object, value: object) -> None:
        """
        Insert (key, value) item into HashTable self.

        >>> ht = HashTable(2)
        >>> ht.capacity == 2
        True
        >>> ht.__setitem__("one", 1)
        >>> ht["two"] = 2
        >>> ht.capacity
        4
        """
        # fine the appropriate bucket
        bucket = self.table[hash(key) % self.capacity]
        # if key is there, replace value (key is already there with different value_
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, value)
        # insert item if it's not already there (is this pair not in the bucket)
        if (key, value) not in bucket:
            bucket.append((key, value))
            # update items and collisions
            self.items += 1
            if len(bucket) > 1:
                self.collisions += 1
        # if the density is high, double the table
        if (self.items / self.capacity) > 0.7:
            self.double()

    def double(self) -> None:
        """
        Double the capacity of this hash table, and re-hash all items.

        @param HashTable self: this hash table
        @rtype: None
        """

        # temporarily save self.table
        old_table = self.table
        # reset items and collisions
        self.items, self.collisions = 0, 0
        # create double-sized table
        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity)]
        # insert old items into new table
        for bucket in old_table:  # douhling the table may result in items pointing differently due to the modulo
            for item in bucket:
                self[item[0]] = item[1]
        # stats after doubling

    def insert(self, item):
        """
        Insert (key, value) item into HashTable self.

        @param HashTable self: this HashTable
        @param (object, object) item: key/value pair, key is hashable
        @rtype: None
        """
        # find the appropriate bucket
        # insert item if it's not already there
            # update collisions
        # if the capacity is high, double it

    def retrieve(self, key):
        """
        Return value corresponding to key, or else raise Exception.

        @param HashTable key: this hash table
        @param object key: hashable key
        @rtype: object
        """
        # get the right bucket
        # get item from bucket
        # raise an error if key not present

    def stats(self):
        """
        Provide statistics.

        @param HashTable self: this hash table
        @rtype: str
        """
        buckets = sum([1 for b in self.table if len(b) > 0])
        max_bucket_length = max([len(b) for b in self.table])
        average = "Average bucket length: {}.\n".format(self.items / buckets)
        ideal = "Density: {}\n".format(self.items / self.capacity)
        collisions = "Collisions: {}\n".format(self.collisions)
        maximum = "Maximum bucket length: {}".format(max_bucket_length)
        return average + ideal + collisions + maximum


def create_dict(n:int)->HashTable:
    """
    Create a dictionary with n keys
    """
    d = HashTable()
    for i in range(n):
        d.insert((i,i))
    return d


def dict_search(d:HashTable)->bool:
    """
    search for the last key in d
    """
    return d.retrieve(np.random.randint(0, 2000))


def plot(results:list)->None:
    """
    Plots a graph
    """
    x = [i[0] for i in results]
    y = [i[1] for i in results]
    plt.plot(x,y)
    plt.show()


def test(f: Callable[[list],Union[int, None]], n:list)->tuple:
    """
    Creates varios data structures and times the search time
    for a random item search in it
    """
    data = create_dict(n)
    taken = 0.0
    for i in range(5):
        start = time()
        f(data)
        taken = taken + (time() - start)
    return n, taken/10

if __name__ == '__main__':


    results = []
    inputs = range(2000, 3000, 10)

    for i in inputs:
        results.append(test(dict_search, i))
    plot(results)
