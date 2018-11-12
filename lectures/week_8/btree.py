"""
BinaryTree class and associated functions.
"""


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

    def __contains__(self, val):
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


def contains(node, val):
    """
    Return whether tree rooted at node contains value. val.
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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
