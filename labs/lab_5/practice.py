def max_depth(obj):
    """
    Return 1 + the maximum depth of obj's elements if obj is a list.
    Otherwise return 0.

    @param object|list obj: list or object to return depth of
    @rtype: int
    >>> max_depth(17)
    0
    >>> max_depth([])
    1
    >>> max_depth([1, "two", 3])
    1
    >>> max_depth([1, ["two", 3], 4])
    2
    >>> max_depth([1, [2, ["three", 4], 5], 6])
    3
    """

    if not isinstance(obj, list):
        return 0
    elif obj == []:
        return 1
    else:
        return 1 + max([max_depth(x) for x in obj])


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
    if isinstance(string_list, list):
        return "".join([concat_strings(x) for x in string_list])
    else:
        return string_list
