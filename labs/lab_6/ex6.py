""" Tree class and functions.
"""
from csc148_queue import Queue
from typing import Any, Callable, List


class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    """

    def __init__(self, value=None, children=None) -> None:
        """
        Create Tree self with content value and 0 or more children
        """
        self.value = value
        # copy children if not None
        self.children = children[:] if children is not None else []

    def __repr__(self) -> str:
        """
        Return representation of Tree (self) as string that
        can be evaluated into an equivalent Tree.

        >>> t1 = Tree(5)
        >>> t1
        Tree(5)
        >>> t2 = Tree(7, [t1])
        >>> t2
        Tree(7, [Tree(5)])
        """
        # Our __repr__ is recursive, because it can also be called
        # via repr...!
        return ('Tree({}, {})'.format(repr(self.value), repr(self.children))
                if self.children
                else 'Tree({})'.format(repr(self.value)))

    def __eq__(self, other: Any) -> bool:
        """
        Return whether this Tree is equivalent to other.
        >>> t1 = Tree(5)
        >>> t2 = Tree(5, [])
        >>> t1 == t2
        True
        >>> t3 = Tree(5, [t1])
        >>> t2 == t3
        False
        """
        return (type(self) is type(other) and
                self.value == other.value and
                self.children == other.children)

    def __str__(self, indent=0) -> str:
        """
        Produce a user-friendly string representation of Tree self,
        indenting each level as a visual clue.

        >>> t = Tree(17)
        >>> print(t)
        17
        >>> t1 = Tree(19, [t, Tree(23)])
        >>> print(t1)
        19
           17
           23
        >>> t3 = Tree(29, [Tree(31), t1])
        >>> print(t3)
        29
           31
           19
              17
              23
        >>> print(descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3))
        0
           1
              4
              5
              6
           2
              7
              8
           3
        """
        root_str = indent * " " + str(self.value)
        return '\n'.join([root_str] +
                         [c.__str__(indent + 3) for c in self.children])

    def __contains__(self, v: object) -> bool:
        """
        Return whether Tre self contains v.

        >>> t = Tree(17)
        >>> t.__contains__(17)
        True
        >>> t = descendants_from_list(Tree(19), [1, 2, 3, 4, 5, 6, 7], 3)
        >>> t.__contains__(5)
        True
        >>> t.__contains__(18)
        False
        """
        #
        # if self.children == []:
        #     return self.value == v
        # else:
        #     return any([tree.__contains__(v) for tree in self.children] + [self.value == v])

        return self.value == v or any([tree.__contains__(v) for tree in self.children])


def list_internal(t: Tree) -> list:
    """
    Return list of values in internal nodes of t.

    >>> t = Tree(0)
    >>> list_internal(t)
    []
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> L = list_internal(t)
    >>> L.sort()
    >>> L
    [0, 1, 2]
    """
    if len(t.children) == 0:
        return []
    else:
        return [t.value] + gather_lists([list_internal(tree) for tree in t.children])


def count_internal(t: Tree) -> int:
    """
    Return number of internal nodes of t.

    >>> t = Tree(0)
    >>> count_internal(t)
    0
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> count_internal(t)
    3
    """
    if len(t.children) == 0:
        return 0
    else:
        return 1 + sum([count_internal(tree) for tree in t.children])


def count_leaves(t: Tree) -> int:
    """
    Return the number of leaves in Tree t.

    >>> t = Tree(7)
    >>> count_leaves(t)
    1
    >>> t = descendants_from_list(Tree(7), [0, 1, 3, 5, 7, 9, 11, 13], 3)
    >>> count_leaves(t)
    6
    """
    if len(t.children) == 0:
        return 1
    else:
        return sum([count_leaves(tree) for tree in t.children])


def sum_internal(t: Tree) -> int:
    """
    Return sum of the internal (non-leaf) nodes of t.

    Assume all nodes have integer values.

    >>> t = Tree(0)
    >>> sum_internal(t)
    0
    >>> t = descendants_from_list(Tree(1), [2, 3, 4, 5, 6, 7, 8, 9], 3)
    >>> sum_internal(t)
    6
    """
    if len(t.children) == 0:
        return 0
    else:
        return t.value + sum([sum_internal(tree) for tree in t.children])


def sum_leaves(t: Tree) -> int:
    """
    Return sum of the leaves of t.
    >>> t = Tree(0)
    >>> sum_leaves(t)
    0
    >>> t = descendants_from_list(Tree(1), [2, 3, 4, 5, 6, 7, 8, 9], 3)
    >>> sum_leaves(t)
    39
    """
    if len(t.children) == 0:
        return t.value
    else:
        return sum([sum_leaves(tree) for tree in t.children])


def pree(t: Tree) -> None:
    """ PREEEE
    >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5), Tree(5.75)])
    >>> tn3 = Tree(3, [Tree(6), Tree(7)])
    >>> tn1 = Tree(1, [tn2, tn3])
    >>> print(tn1)
    1
       2
          4
          4.5
          5
          5.75
       3
          6
          7
    >>> pree(tn1)
    """
    print(t.value)
    for c in t.children:
        pree(c)


def arity(t: Tree) -> int:
    """
    Return the maximum branching factor (arity) of Tree t.

    >>> t = Tree(23)
    >>> arity(t)
    0
    >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5), Tree(5.75)])
    >>> tn3 = Tree(3, [Tree(6), Tree(7)])
    >>> tn1 = Tree(1, [tn2, tn3])
    >>> print(tn1)
    1
       2
          4
          4.5
          5
          5.75
       3
          6
          7
    >>> arity(tn1)
    4
    >>> tn4 = Tree(0, [tn1, Tree(0.1), Tree(0.2), Tree(0.3), Tree(0.4), Tree(0.5)])
    >>> arity(tn4)
    6
    >>> tn5 = Tree(-1, [tn1])
    >>> arity(tn5)
    4
    """
    if all([len(child.children) == 0 for child in t.children]):
        return len(t.children)
    else:
        return max(len(t.children), max([arity(tree) for tree in t.children]))


def contains_test_passer(t: Tree, test: Callable[[Any], bool]) -> bool:
    """
    Return whether t contains a value that test(value) returns True for.

    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4.5, 5, 6, 7.5, 8.5], 4)
    >>> print(t)
    0
       1
          5
          6
          7.5
          8.5
       2
       3
       4.5
    >>> def greater_than_nine(n): return n > 9
    >>> contains_test_passer(t, greater_than_nine)
    False
    >>> def even(n): return n % 2 == 0
    >>> contains_test_passer(t, even)
    True
    """
    # if len(t.children) == 0:
    #     return test(t.value)
    # else:
    #     return any([contains_test_passer(tree, test) for tree in t.children])
    return test(t.value) or any([contains_test_passer(tree, test) for tree in t.children])
    # any([tree.__contains__(v) for tree in self.children])


def list_if(t: Tree, p: Callable[[Any], bool]) -> list:
    """
    Return a list of values in Tree t that satisfy predicate p(value).

    Assume p is defined on all of t's values.

    >>> def p(v): return v > 4
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> list_ = list_if(t, p)
    >>> set(list_) == {5, 6, 7, 8}
    True
    >>> def p(v): return v % 2 == 0
    >>> list_ = list_if(t, p)
    >>> set(list_) == {0, 2, 4, 6, 8}
    True
    """
    # if p(t.value):
    #     val = [t.value]
    # else:
    #     val = []
    # if len(t.children) == 0:
    #     return val
    # else:
    #     return gather_lists([list_if(tree, p) for tree in t.children] + [val])
    return gather_lists([list_if(tree, p) for tree in t.children] +
                        [[t.value] if p(t.value) else []])


def count_if(t: Tree, p: Callable[[object], bool]) -> int:
    """
    Return number of values in Tree t that satisfy predicate p(value).
    Assume predicate p is defined on t's values
    >>> def p(v): return v > 4
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> count_if(t, p)
    4
    >>> def p(v): return v % 2 == 0
    >>> count_if(t, p)
    5
    """
    return (1 if p(t.value) else 0) + sum([count_if(tree, p) for tree in t.children])


def preorder_visit(t: Tree, act: Callable[[Tree], Any]) -> None:
        """
        Visit each node of Tree t in preorder, and act on the nodes
        as they are visited.
        >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
        >>> def act(node): print(node.value)
        >>> preorder_visit(t, act)
        0
        1
        4
        5
        6
        2
        7
        3
        """
        # act(t)
        # for c in t.children:
        #     preorder_visit(c, act)
        # act on t, then visit t's children in predorder
        act(t)
        # visit
        for child in t.children:
            preorder_visit(child, act)


def postorder_visit(t: Tree, act: Callable[[Tree], Any]) -> None:
    """
    Visit each node of t in postorder, and act on it when it is visited.
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> postorder_visit(t, act)
    4
    5
    6
    1
    7
    2
    3
    0
    """
    # visit, in postorder, t's children, then act on t
    for child in t.children:
        postorder_visit(child, act)
    act(t)


def levelorder_visit(t: Tree, act: Callable[[Tree], Any]) -> None:
    """
    Visit every node in Tree t in level order and act on the node
    as you visit it.
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> levelorder_visit(t, act)
    0
    1
    2
    3
    4
    5
    6
    7
    """
    to_act = Queue()
    to_act.add(t)
    while not to_act.is_empty():
        tree = to_act.remove()
        tree: Tree
        act(tree)
        for child in tree.children:
            to_act.add(child)


def visit_level(t: Tree, act: Callable[[Tree], Any], n: int) -> int:
    """
    Visit every node in Tree t at level n, return the number of of nodes visited.
    Assume n is non-negative.

    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> visit_level(t, act, 1)
    1
    2
    3
    3
    """
    # on depth 0, we act,
    if n == 0:
        act(t)
        return 1
    # otherwise we keep on going until we reach the required level.
    else:
        return sum([visit_level(child, act, n - 1) for child in t.children])


def levelorder_visit2(t: Tree, act: Callable[[Tree], Any]) -> None:
    """
    Visit every node in Tree t in level order and act on the node
    as you visit it.
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> levelorder_visit2(t, act)
    0
    1
    2
    3
    4
    5
    6
    7
    """
    level_to_visit = 0
    visited = 1
    while visited > 0:
        visited = visit_level(t, act, level_to_visit)
        level_to_visit += 1


# helper function that may be useful in the functions
# above
def gather_lists(list_: List[list]) -> list:
    """
    Concatenate all the sublists of L and return the result.

    >>> gather_lists([[1, 2], [3, 4, 5]])
    [1, 2, 3, 4, 5]
    >>> gather_lists([[6, 7], [8], [9, 10, 11]])
    [6, 7, 8, 9, 10, 11]
    """
    new_list = []
    for l in list_:
        new_list += l
    return new_list
    # equivalent to...
    # return sum([list_ for list_ in list_], [])


# helpful helper function
def descendants_from_list(t: Tree, list_: list, branching: int) -> Tree:
    """
    Populate Tree t's descendants from list_, filling them
    in in level order, with up to arity children per node.
    Then return t.

    >>> descendants_from_list(Tree(0), [1, 2, 3, 4], 2)
    Tree(0, [Tree(1, [Tree(3), Tree(4)]), Tree(2)])
    >>> descendants_from_list(Tree(0), [1, 2, 3, 4], 1)
    Tree(0, [Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])])
    >>> descendants_from_list(Tree(0), [1, 2, 3, 4], 3)
    Tree(0, [Tree(1, [Tree(4)]), Tree(2), Tree(3)])
    >>> descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    """
    q = Queue()
    q.add(t)
    list_ = list_.copy()
    while not q.is_empty():  # unlikely to happen
        new_t = q.remove()
        new_t: Tree
        for _ in range(0, branching):
            if len(list_) == 0:
                return t  # our work here is done
            else:
                new_t_child = Tree(list_.pop(0))
                new_t.children.append(new_t_child)
                q.add(new_t_child)
    return t


def count_odd_above(t, n):
    """
    Return the number of nodes with depth less than n that have odd values.
    Assume t’s nodes have integer values.
    @param Tree t: tree to list values from
    @param int n: depth above which to list values
    @rtype: int
    >>> t1 = Tree(4)
    >>> t2 = Tree(3)
    >>> t3 = Tree(5, [t1, t2])
    >>> count_odd_above(t3, 1)
    1
    >>> t4 = Tree(0, [t1, t2, t3, t3])
    >>> count_odd_above(t4, 2)
    2
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1 if t.value % 2 == 1 else 0
    else:
        return sum([count_odd_above(x, n - 1) for x in t.children])


def count_at_depth(t, d):
    """ Return the number of nodes at depth d of t.
    @param Tree t: tree to explore --- cannot be None
    @param int d: depth to report from, non-negative
    @rtype: int
    >>> t = Tree(17, [Tree(0), Tree(1, [Tree(4)]), Tree(2, [Tree(5)]), Tree(3)])
    >>> print(t)
    17
       0
       1
          4
       2
          5
       3
    >>> count_at_depth(t, 0)
    1
    >>> count_at_depth(t, 1)
    4
    >>> count_at_depth(t, 2)
    2
    >>> count_at_depth(t, 5)
    0
    """
    if d < 0:
        return 0
    elif d == 0:
        return 1
    else:
        return sum([count_at_depth(c, d - 1) for c in t.children])


if __name__ == '__main__':
    import python_ta
    python_ta.check_all()
    import doctest
    doctest.testmod()
