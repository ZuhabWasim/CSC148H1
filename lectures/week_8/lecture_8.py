""" Lecture 8 Notes

-one approach to BinaryTree would to make a subclass of Tree
    -any client code that uses Tree would be required not to violate the branching factor (2) of the binary Tree
    -Make the Tree immutable, make sure there is no way to change children or value
    -they have subclasses that might be mutable

-Special standard methods of a binary tree
    -__init__ : basic
    -__eq__: checks equivalence of data, and left and right nodes
    -__repr__: calls repr recursively to find the representation of the whole btree

-Remember that the first parameter 'self' does not necessarily need to be called self
 it can be called anything as long as it is the same object.

-you can translate mathematical ooperational precedence using binary trees
   '+'
  /   \
 '*'   7
 / \
3   4
- everything in python are bojects except operators (+, -, /, %)
- if yu want to store those operators in the tree, you have two options
    - access using the special methods i.e. 7.0.__add__(9.5)
    - use the built in method eval("7 + 9")
- this has some properties
    - there are no empty expressions (no None)
    - if it's a leaf, just return the value
    - o/w
        - evaluate the left tree
        - evaluate the right tree
        - combine them using eval


- when you get the error "expected type ___, got object", assign a local type contract to the value.
- when writing return None, python likes it if right pass instead


- inorder:
    - A recursive denition:
        visit the left subtree inorder
        visit this node itself
        visit the right subtree inorder

- Adding ordering conditions to a binary tree
    - data are comparable
    - data in left subtree are less than node.data
    - data in right subtree is greater than node.data

- a BST of height 1 has height 1
- ""              3            2
- ""              7            3
- ""             15            4
- ""              n    ceil(log_2(n)) (also known as ceil(lgn))

-very efficient, a tree with 1 million nodes can be organized in a tree of height 20,
- i.e. if you're searching for a value in some node, you can do it in lgn steps.
"""
