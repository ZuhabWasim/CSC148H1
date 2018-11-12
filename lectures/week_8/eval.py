"""
BinaryTree class and associated functions.
"""
from typing import Union
from bst import BTNode


class BinaryTree:
    """
    A Binary Tree, i.e. arity 2.
    """
    def __init__(self, value, left=None, right=None):
        """
        Create BinaryTree self with value and children left and right.
        @param BinaryTree self: this binary tree
        @param object value: value of this node
        @param BinaryTree|None left: left child
        @param BinaryTree|None right: right child
        @rtype: None
        """
        self.value, self.left, self.right = value, left, right

    def __eq__(self, other):
        """
        Return whether BinaryTree self is equivalent to other.
        @param BinaryTree self: this binary tree
        @param Any other: object to check equivalence to self
        @rtype: bool
        >>> BinaryTree(7).__eq__("seven")
        False
        >>> b1 = BinaryTree(7, BinaryTree(5))
        >>> b1.__eq__(BinaryTree(7, BinaryTree(5), None))
        True
        """
        return (type(self) == type(other) and
                self.value == other.value and
                (self.left, self.right) == (other.left, other.right))

    def __repr__(self):
        """
        Represent BinaryTree (self) as a string that can be evaluated to
        produce an equivalent BinaryTree.
        @param BinaryTree self: this binary tree
        @rtype: str
        >>> BinaryTree(1, BinaryTree(2), BinaryTree(3))
        BinaryTree(1, BinaryTree(2, None, None), BinaryTree(3, None, None))
        """
        return "BinaryTree({}, {}, {})".format(repr(self.value),
                                               repr(self.left),
                                               repr(self.right))

    def __str__(self, indent=""):
        """
        Return a user-friendly string representing BinaryTree (self)
        inorder.  Indent by indent.
        >>> childTree1 = BinaryTree(2,BinaryTree(3))
        >>> childTree2 = BinaryTree(4)
        >>> b = BinaryTree(1,childTree1, childTree2)

        >>> print(b)
            4
        1
            2
                3
        <BLANKLINE>
        """
        right_tree = (self.right.__str__(
            indent + "    ") if self.right else "")
        left_tree = self.left.__str__(indent + "    ") if self.left else ""
        return (right_tree + "{}{}\n".format(indent, str(self.value)) +
                left_tree)

    def __contains__(self, val: object)->bool:
        """
        Return whether tree rooted at self contains value.
        @param BinaryTree self: binary tree to search for value
        @param object val: value to search for
        @rtype: bool
        >>> t = BinaryTree(5, BinaryTree(7), BinaryTree(9))
        >>> t.__contains__(7)
        True
        """
        if self.right is None and self.left is None:
            return self.value == val
        elif self.right is None:
            return self.value == val or self.left.__contains__(val)
        elif self.left is None:
            return self.value == val or self.right.__contains__(val)
        else:
            return self.value == val or any([self.right.__contains__(val),
                                             self.left.__contains__(val)])
        # one liner
        # return (self.value == val
        #        or (self.left is not None and val in self.left)
        #        or (self.right is not None and val in self.right))


def contains(node: Union[BinaryTree, None], val: object) -> bool:
    """
    Return whether tree rooted at node contains value.
    @param BinaryTree|None node: binary tree to search for value
    @param object val: value to search for
    @rtype: bool
    >>> contains(None, 5)
    False
    >>> contains(BinaryTree(5, BinaryTree(7), BinaryTree(9)), 7)
    True
    """
    if node is None:
        return False
    else:
        return node.value == val or any([contains(node.right, val),
                                         contains(node.left, val)])


def height(node: Union[BinaryTree, None]) -> int:
    """
    Return the height of the binary tree rooted at node
    @param BinaryTree node: A binary tree node
    @return: int

    >>> height(None)
    0
    >>> height(BinaryTree(5, BinaryTree(7, BinaryTree(8)), BinaryTree(9)))
    3
    """
    if node is None:
        return 0
    else:
        return 1 + max(height(node.left), height(node.right))


def find(node: Union[BinaryTree, None],
         val: object) -> Union[BinaryTree, None]:
    """
    Return a BinaryTree node that contains the given value
    @param BinaryTree node: A binary tree node
    @param object val: value to search
    @return: BinaryTree

    >>> find(None, 5) is None
    True
    >>> find(BinaryTree(5, BinaryTree(7), BinaryTree(9)), 7)
    BinaryTree(7, None, None)
    """
    if node is None:
        return None
    else:
        result = find(node.left, val)
        if node.value == val:
            return node
        elif result is not None:
            return find(node.left, val)
        elif result is not None:
            return find(node.right, val)
        return None


def evaluate(b: BinaryTree) -> float:
    """
    Evaluate the expression rooted at b.  If b is a leaf,
    return its float value.  Otherwise, evaluate b.left and
    b.right and combine them with b.value.

    Assume:  -- b is a non-empty binary tree
             -- interior nodes contain value in {"+", "-", "*", "/"}
             -- interior nodes always have two children
             -- leaves contain float value

     @param BinaryTree b: binary tree representing arithmetic expression
     @rtype: float

    >>> b = BinaryTree(3.0)
    >>> evaluate(b)
    3.0
    >>> b = BinaryTree("*", BinaryTree(3.0), BinaryTree(4.0))
    >>> evaluate(b)
    12.0
    """
    b.value: Union[str, float]
    if b.left is None and b.right is None:
        return b.value
    else:
        return eval(str(evaluate(b.left))
                    + b.value
                    + str(evaluate(b.right)))


def parenthesize(b: BTNode) -> str:
    """
    >>> b = BTNode(3.0)
    >>> print(parenthesize(b))
    3.0
    """

    # leaf? if left is missing so must the right!
    if b.left is None:
        return str(b.data)
    else:
        # General expression
        return "({} {} {})".format(parenthesize(b.left),
                                   b.data,
                                   parenthesize(b.right))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
