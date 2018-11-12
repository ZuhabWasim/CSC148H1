# module-level functions, alternatively these could be implemented as
# methods, but then they might not be appropriate for every Tree
from tree import Tree, descendants_from_list
from csc148_queue import Queue


def leaf_count(t):
    """
    Return the number of leaves in Tree t.

    @param Tree t: tree to count number of leaves of
    @rtype: int

    >>> t = Tree(7)
    >>> leaf_count(t)
    1
    >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5)])
    >>> tn3 = Tree(3, [Tree(6), Tree(7)])
    >>> tn1 = Tree(1, [tn2, tn3])
    >>> leaf_count(tn1)
    5
    """
    if t.children == []:
        return 1
    else:
        return sum([leaf_count(c) for c in t.children])


def pre_print(t):
    """
    Print the nodes in preorder.

    >>> t = Tree(13)
    >>> pre_print(t)
    13
    >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5)])
    >>> tn3 = Tree(3, [Tree(6), Tree(7)])
    >>> tn1 = Tree(1, [tn2, tn3])
    >>> pre_print(tn1)
    1
    2
    4
    4.5
    5
    3
    6
    7
    """
    # if t.children == []:
    #     return 1
    # else:
    #     return 1 + max([height(c) for c in t.children])
    print(t.value)
    for c in t.children:
        pre_print(c)


def pre_list(t):
    """
    Print the nodes in preorder.

    >>> t = Tree(13)
    >>> pre_print(t)
    13
    >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5)])
    >>> tn3 = Tree(3, [Tree(6), Tree(7)])
    >>> tn1 = Tree(1, [tn2, tn3])
    >>> pre_print(tn1)
    1
    2
    4
    4.5
    5
    3
    6
    7
    """
    # if t.children == []:
    #     return 1
    # else:
    #     return 1 + max([height(c) for c in t.children])
    if t is None:
        return []
    return [t.value] + [pre_list(c) for c in t.children]


def height(t):
    """
    Return 1 + length of longest path of t.

    @param Tree t: tree to find height of
    @rtype: int

    >>> t = Tree(13)
    >>> height(t)
    1
    >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5)])
    >>> tn3 = Tree(3, [Tree(6), Tree(7)])
    >>> tn1 = Tree(1, [tn2, tn3])
    >>> height(tn1)
    3
    """
    if t.children == []:
        return 1
    else:
        return 1 + max([height(c) for c in t.children])


def arity(t):
    """
    Return the maximum branching factor (arity) of Tree t.

    @param Tree t: tree to find the arity of
    @rtype: int

    >>> t = Tree(23)
    >>> arity(t)
    0
    >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5)])
    >>> tn3 = Tree(3, [Tree(6), Tree(7)])
    >>> tn1 = Tree(1, [tn2, tn3])
    >>> arity(tn1)
    3
    """
    if t.children == []:
        return 0
    else:
        return max(len(t.children), max(arity(c) for c in t.children))




if __name__ == '__main__':
    import doctest

    doctest.testmod()
