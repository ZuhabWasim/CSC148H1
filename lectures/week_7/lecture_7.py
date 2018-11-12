""" Lecture notes
Diagrams of trees with nodes and edges, edges that can have a direction and weight.

terminology
 - set of nodes (possibly with values or labels), with directed edges
   between some pairs of nodes
 - One node is distinguished as root
 - Each non-root node has exactly one parent.
 - A path is a sequence of nodes n1, n2, n3, nk, where there is an edge from ni to ni+1. The length of a path is the number of
   edges in it
 - There is a unique path from the root to each node. In the case of
    - one + only 1
   the root itself this is just n1, if the root is node n1.
 - There are no cycles | no paths that form loops.

more terminology
 - leaf: node with no children
 - internal node: node with one or more children
 - subtree: tree formed by any tree node together with its
 - descendants and the edges leading to them.
 - height: 1 + the maximum path length from the root to some leaf.
        controversy: the definition of height differs in convention,
        tree of one childless node is height of 1
        empty tree is 0
 - depth: length of a path from root to a node is the node's depth.
 - arity, branching factor: maximum number of children for any node.

- if we want access to a tree, we access the tree itself, we can think of accessing the childrens recursively by
accessing the subtrees in the tree.

- avoid having the default children parameter as mutable.
    - if the default parameter is mutable, the contents will always persist as long as the function itself exists
    - def f(n, L = []):
            L.append(n)
            return L
    - will constantly return values appended to the default list

- general structure of recursion
if (condition to detect a base case):
    (do something without recursion)
else: # (general case)
    (do something that involves recursive call(s))

- things that are too embedded into a class should a class level method rather than a module level function.

- implementation of trees is used in directories of windows folders
- python has a module called os that can scan directories

777 the number of the beast plus 111

- functions are objects, take in names and carry out instructions on them
- you can pass in function names as if it was an object.



- traversal
The functions and methods we have seen get information from
every node of the tree | in some sense they traverse the tree.
Sometimes the order of processing tree nodes is important: do
we process the root of the tree (and the root of each subtree...)
before or after its children? Or, perhaps, we process along levels
that are the same distance from the root?
- preorder of a tree
    - visit the node first and then the children

- postorder of a tree
    - visit children in post order, then visit the node

- level order
    - process the all the nodes at a specified level
"""
from typing import Callable, Any
from tree import Tree

def preorder_visit(t: Tree, act: Callable[[Tree], Any]) -> None:
    """
    Visit each node of Tree t in preorder, and act on the nodes
    as they are visited.
    >>> t = descendants_from_list(Tree(0),
    [1, 2, 3, 4, 5, 6, 7], 3)
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
    act(t)
    for c in t.children:
        preorder_visit(c, act)
