"""
BTNode exercises
"""
from typing import Union, Any


class BTNode:
    """Binary Tree node.

    data - data this node represents
    left - left child
    right - right child
    """
    data: object
    left: Union["BTNode", None]
    right: Union["BTNode", None]

    def __init__(self, data: object,
                 left: Union["BTNode", None]=None,
                 right: Union["BTNode", None]=None) -> None:
        """
        Create BTNode (self) with data and children left and right.

        An empty BTNode is represented by None.

        """
        self.data, self.left, self.right = data, left, right

    def __eq__(self, other: Any) -> bool:
        """
        Return whether BTNode (self) is equivalent to other.

        >>> BTNode(7).__eq__('seven')
        False
        >>> b1 = BTNode(7, BTNode(5))
        >>> b1.__eq__(BTNode(7, BTNode(5), None))
        True
        """
        return (type(self) == type(other) and
                self.data == other.data and
                (self.left, self.right) == (other.left, other.right))

    def __repr__(self) -> str:
        """
        Represent BTNode (self) as a string that can be evaluated to
        produce an equivalent BTNode.

        >>> BTNode(1, BTNode(2), BTNode(3))
        BTNode(1, BTNode(2, None, None), BTNode(3, None, None))
        """
        return 'BTNode({}, {}, {})'.format(self.data,
                                           repr(self.left),
                                           repr(self.right))

    def __str__(self, indent: str="") -> str:
        """
        Return a user-friendly string representing BTNode (self) inorder.
        Indent by indent.

        >>> b = BTNode(1, BTNode(2, BTNode(3)), BTNode(4))
        >>> print(b)
            4
        1
            2
                3
        <BLANKLINE>
        """
        right_tree = self.right.__str__(indent + '    ') if self.right else ''
        left_tree = self.left.__str__(indent + '    ') if self.left else ''
        return right_tree + '{}{}\n'.format(indent, str(self.data)) + left_tree


def binary_sum(node: Union[BTNode, None], d: int) -> int:
    """ asd

    >>> binary_sum(None, 2)
    0
    >>> binary_sum(BTNode(5), 0)
    5
    >>> b1 = BTNode(7)
    >>> b2 = BTNode(3, BTNode(2), None)
    >>> b3 = BTNode(5, b2, b1)
    >>> binary_sum(b3, 1)
    10
    """
    node.data: int
    if d < 0 or node is None:
        return 0
    elif d == 0:
        return node.data
    else:
        return binary_sum(node.left, d - 1) + binary_sum(node.right, d - 1)


def list_longest_path(node: Union[BTNode, None]) -> list:
    """ List the data in a longest path of node.

    >>> list_longest_path(None)
    []
    >>> list_longest_path(BTNode(5))
    [5]
    >>> b1 = BTNode(7)
    >>> b2 = BTNode(3, BTNode(2), None)
    >>> b3 = BTNode(5, b2, b1)
    >>> print(b3)
        7
    5
        3
            2
    <BLANKLINE>
    >>> list_longest_path(b3)
    [5, 3, 2]
    """
    if node is None:
        return []
    left = list_longest_path(node.left)
    right = list_longest_path(node.right)
    if len(left) > len(right):
        return [node.data] + left
    # elif len(right) > len(left):
    #     return [node.data] + right
    # return [node.data]
    return [node.data] + right


def get_height(node: Union[BTNode, None]) -> int:
    """ get the height of node

    >>> get_height(None)
    -1
    >>> get_height(BTNode(5))
    0
    >>> b1 = BTNode(7)
    >>> b2 = BTNode(3, BTNode(2), None)
    >>> b3 = BTNode(5, b2, b1)
    >>> print(b3)
        7
    5
        3
            2
    <BLANKLINE>
    >>> get_height(b3)
    2
    """
    if node is None:
        return -1
    elif node.left is None and node.right is None:
        return 0
    else:
        return 1 + max(get_height(node.left), get_height(node.right))


def get_num(t: Union[BTNode, None], h: int) -> int:
    """ get min number of nodes required to full tree."""
    if h == 0:
        if t is None:
            return 1
        else:
            return 0
    else:
        if t is None:
            return get_num(None, h - 1) + get_num(None, h - 1)
        return get_num(t.right, h - 1) + get_num(t.left, h - 1)


def make_full(t: Union[BTNode, None]) -> int:
    """ full

    >>> b1 = BTNode(7)
    >>> b2 = BTNode(3, BTNode(2), None)
    >>> b3 = BTNode(5, b2, b1)
    >>> make_full(b3)
    3
    >>> b_left = None#BTNode(4, BTNode(2), BTNode(6))
    >>> b_right = BTNode(12, BTNode(10), BTNode(14))
    >>> b = BTNode(8, b_left, b_right)
    >>> print(b)
            14
        12
            10
    8
    <BLANKLINE>
    >>> make_full(b)
    3
    """
    h = get_height(t)
    if h == -1:
        return 1
    elif h == 0:
        return 0
    else:
        s = 0
        for i in range(h + 1):
            s += get_num(t, i)
        return s


def list_between(node: Union[BTNode, None], start: object, end: object) -> list:
    """
    Return a Python list of all data in the binary search tree
    rooted at node that are between start and end (inclusive).

    A binary search tree t is a BTNode where all nodes in the subtree
    rooted at t.left are less than t.data, and all nodes in the subtree
    rooted at t.right are more than t.data

    Avoid visiting nodes with values less than start or greater than end.

    >>> b_left = BTNode(4, BTNode(2), BTNode(6))
    >>> b_right = BTNode(12, BTNode(10), BTNode(14))
    >>> b = BTNode(8, b_left, b_right)
    >>> print(b)
            14
        12
            10
    8
            6
        4
            2
    <BLANKLINE>
    >>> list_between(None, 3, 13)
    []
    >>> list_between(b, 2, 3)
    [2]
    >>> L = list_between(b, 3, 11)
    >>> L.sort()
    >>> L
    [4, 6, 8, 10]
    """
    # if node is None:
    #     return []
    # elif not (start <= node.data <= end):
    #     return (list_between(node.left, start, end) +
    #             list_between(node.right, start, end))
    # else:
    #     return (list_between(node.left, start, end)
    #             + [node.data] +
    #             list_between(node.right, start, end))

    if node is None:
        return []
    elif start <= node.data <= end:
        return (list_between(node.left, start, end)
                + [node.data] +
                list_between(node.right, start, end))
    elif start > node.data:
        return list_between(node.right, start, end)
    return list_between(node.left, start, end)  # end < node.data


def count_shallower(t: Union[BTNode, None], n: int) -> int:
    """ Return the number of nodes in tree rooted at t with
    depth less than n.

    >>> t = BTNode(0, BTNode(1, BTNode(2)), BTNode(3))
    >>> print(t)
        3
    0
        1
            2
    <BLANKLINE>
    >>> count_shallower(t, 2)
    3
    """
    # if t is None or n == 0:
    #     return []
    # else:
    #     return (count_shallower(t.left, n - 1) +
    #             [t.data] +
    #             count_shallower(t.right, n - 1))
    if t is None or n == 0:
        return 0
    else:
        return (count_shallower(t.left, n - 1) +
                1 +
                count_shallower(t.right, n - 1))


def concatenate_leaves(t: Union[BTNode, None]) -> str:
    """
    Return the string values in the Tree rooted at t concatenated from left to right.
    Assume all leaves have string value.

    >>> t1 = BTNode("one")
    >>> t2 = BTNode("two")
    >>> t3 = BTNode("three", t1, t2)
    >>> print(t3)
        two
    three
        one
    <BLANKLINE>
    >>> concatenate_leaves(t1)
    'one'
    >>> concatenate_leaves(t3)
    'onetwo'
    >>> b_left = BTNode(4, BTNode(2), BTNode(6))
    >>> b_right = BTNode(12, BTNode(10), BTNode(14))
    >>> b = BTNode(8, b_left, b_right)
    >>> print(b)
            14
        12
            10
    8
            6
        4
            2
    <BLANKLINE>
    >>> concatenate_leaves(b)
    '261014'
    """
    if t is None:
        return ''
    elif t.right is None and t.left is None:
        return str(t.data)
    return concatenate_leaves(t.left) + concatenate_leaves(t.right)


def count_leaves(t: Union[BTNode, None]) -> int:
    """
    Return the number of leaves in BinaryTree t.

    >>> t1 = BTNode(1)
    >>> t2 = BTNode(2)
    >>> t3 = BTNode(3, t1, t2)
    >>> count_leaves(None)
    0
    >>> count_leaves(t3)
    2
    """
    if t is None:
        return 0
    elif t.right is None and t.left is None:
        return 1
    return count_leaves(t.left) + count_leaves(t.right)


def sum_leaves(t: Union[BTNode, None]) -> int:
    """
    Return the sum of the values in the leaves of BinaryTree t.  Return
    0 if t is empty.
    Assume all leaves have integer value.

    >>> t1 = BTNode(1)
    >>> t2 = BTNode(2)
    >>> t3 = BTNode(3, t1, t2)
    >>> sum_leaves(t2)
    2
    >>> sum_leaves(t3)
    3
    """
    t.data: int
    if t is None:
        return 0
    elif t.right is None and t.left is None:
        return t.data
    return sum_leaves(t.left) + sum_leaves(t.right)


def sum_internal(t: Union[BTNode, None]) -> int:
    """
    Return the sum of the values in the internal nodes of BinaryTree t.  Return
    0 if t is empty.
    Assume all internal nodes have integer value.

    >>> t1 = BTNode(1)
    >>> t2 = BTNode(2)
    >>> t3 = BTNode(3, t1, t2)
    >>> sum_internal(t2)
    0
    >>> sum_internal(t3)
    3
    """
    t.data: int
    if t is None:
        return 0
    elif t.right is not None or t.left is not None:
        return sum_internal(t.left) + t.data + sum_internal(t.right)
    return 0


def contains_satisfier(list_, predicate):
    """
    Return whether possibly-nested list_ contains a non-list element
    that satisfies (returns True for) predicate.
    @param list list_: list to check for predicate satisfiers
    @param (object)->bool predicate: boolean function
    @rtype: bool
    >>> list_ = [5, [6, [7, 8]], 3]
    >>> def p(n): return n > 7
    >>> contains_satisfier(list_, p)
    True
    >>> def p(n): return n > 10
    >>> contains_satisfier(list_, p)
    False
    """
    if isinstance(list_, list):
        return any([contains_satisfier(x, predicate) for x in list_])
    else:
        return predicate(list_)


def btnode_string_distance(node: Union[BTNode, None], d: int) -> str:
    """ asd

    >>> btnode_string_distance(None, 1)
    ''
    >>> bt = BTNode("a", BTNode("b"), BTNode("c"))
    >>> btnode_string_distance(bt, 0)
    'a'
    >>> btnode_string_distance(bt, 1)
    'bc'
    >>> btnode_string_distance(bt, 2)
    ''
    """
    node.data: str
    if d < 0 or node is None:
        return ''
    elif d == 0:
        return node.data
    else:
        return (btnode_string_distance(node.left, d - 1) +
                btnode_string_distance(node.right, d - 1))


if __name__ == "__main__":
    # import python_ta
    # python_ta.check_all(config='pylint.txt')
    import doctest
    doctest.testmod()
