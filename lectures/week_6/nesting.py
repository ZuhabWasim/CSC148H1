"""
some recursive functions on nested lists
"""
from typing import List, Any


def depth(obj):
    """
    Return 0 if obj is a non-list, or 1 + maximum
    depth of elements of obj, a possibly nested
    list of objects. Or 1 if obj == [] (can't take the max of []).

    Assume obj has finite nesting depth

    @param list[object]|object obj: possibly nested list of objects
    @rtype: int

    >>> depth(3)
    0
    >>> depth([])
    1
    >>> depth([[], [[]]])
    3
    >>> depth([1, 2, 3])
    1
    >>> depth([1, [2, 3], 4])
    2
    """
    if obj == []:
        return 1
    elif isinstance(obj, list):
        return 1 + max([depth(x) for x in obj])
    else:
        return 0


def rec_max(obj):
    """
    Return obj if it's an int, or the maximum int in obj,
    a possibly nested list of numbers.

    Assume: obj is an int or non-empty list with finite nesting depth,
    and obj doesn't contain any empty lists

    @param int|list[int|list[...]] obj: possibly nested list of int
    @rtype: int

    >>> rec_max([17, 21, 0])
    21
    >>> rec_max([17, [21, 24], 0])
    24
    >>> rec_max(31)
    31
    """
    if isinstance(obj, list):
        return max([rec_max(x) for x in obj])
    else:
        return obj


def concat_strings(string_list):
    """
    Concatenate all the strings in possibly-nested string_list.

    @param list[str]|str string_list:
    @rtype: str

    >>> concat_strings("brown")
    'brown'
    >>> concat_strings(["now", "brown"])
    'nowbrown'
    >>> concat_strings(["how", ["now", "brown"], "cow"])
    'hownowbrowncow'
    """
    # if not isinstance(string_list, list):
    #     return string_list
    # else:
    #     return "".join([concat_strings(item) for item in string_list])

    return "".join([concat_strings(item)
                    if isinstance(item, list)
                    else item
                    for item in string_list])


def flatten(list_: List[list]) -> list:
    """
    Return a depth-1 list of the elements of list_

    >>> flatten([1, [2, 3, [4]]])
    [1, 2, 3, 4]
    """
    # maybe functional if helps here...
    return sum([[item] if not isinstance(item, list)
                else flatten(item)
                for item in list_], [])


def nested_contains(list_, value):
    """
    Return whether list_, or any nested sub-list of list_ contains value.

    Assume value is a non-list

    @param list list_: list to search
    @param object value: non-list value to search for
    @rtype: bool

    >>> list_ = ["how", ["now", "brown"], 1]
    >>> nested_contains(list_, "brown")
    True
    >>> nested_contains([], 5)
    False
    >>> nested_contains([5], 5)
    True
    """
    # check out Python built-in any
    # if all([not isinstance(x, list) for x in list_]):
    #     return value in list_
    # else:
    #     return any([nested_contains(x, value)
    #                 if isinstance(x, list)
    #                 else (x == value)
    #                 for x in list_])
    return any([nested_contains(x, value)
                if isinstance(x, list)
                else x == value
                for x in list_])
    # Go through the next list if it is a list, otherwise just return if x is equal to value.


def nested_count(list_):
    """
    Return the number of non-list elements of list_ or its nested sub-lists.

    @param list list_: possibly nested list to count elements of
    @rtype: int

    >>> list_ = ["how", ["now", "brown"], "cow"]
    >>> nested_count(list_)
    4
    """
    # functional if helps here
    # if not isinstance(list_, list):
    #     return 1
    # else:
    #     return sum([nested_count(item) for item in list_])
    return sum([1 if not isinstance(item, list)
                else nested_count(item)
                for item in list_])


def list_level(obj: List[Any], d: int) -> List:
    """
    Return the non-list elements at a particular level.

    @param list obj: possibly nested list
    @param int d: The level to print out
    @rtype: List

    >>> list_ = [1, [2, [3, 4], 5], 2]
    >>> list_level(list_, 2)
    [2, 5]
    >>> list_level(list_, 3)
    [3, 4]
    """
    if d < 1:  # If we are passed the depth, we return the null list
        return []
    elif d == 1:  # If we are at the level we want to be, return a list of non-list items.
        return [item for item in obj if not isinstance(item, list)]
    else:  # If we are above the level we want to be, we dive in to the next item if it is a list.
        return sum([list_level(item, d - 1) for item in obj if isinstance(item, list)], [])
    # if d > 1:
    #     if isinstance(obj, list):
    #         return [list_level(item, d - 1) for item in obj]
    #     else:
    #         return []
    # else:
    #     if isinstance(obj, list):
    #         return [item for item in obj if not isinstance(item, list)]
    #     else:
    #         return []


def list_levels(obj: List[Any]) -> List:
    """
        Return the non-list elements at all levels as a list.
        Return levels 1 through depth of obj.

        @param list obj: possibly nested list
        @rtype: List

        >>> list_ = [1, [2, [3, 4], 5], 2]
        >>> list_levels(list_)
        [[1, 2], [2, 5], [3, 4]]
        >>> list_levels([1, [2, 3, [4, 5, [6]]]])
        [[1], [2, 3], [4, 5], [6]]
    """
    return [list_level(obj, d)
            for d in range(1, depth(obj) + 1)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
