""" notes
how efficient is:
tree class:
    -not very efficient, look at all nodes since it is not ordered
    -O(n)
BTNode:
    -same, look at all nodes
    -O(n)
BST
    -depends on the input
    -unbalanced tree --> n steps
    -balanced tree --> lgn steps

node packing
-maximum number of nodes in a binary tree of height:
0 --> special case
1 --> 1 < 2^1 <= 2*1
2 --> 2,3 < 2^2 <= 2*n
3 --> 4,5,6,7 < 2^3 <= 2*n
4 --> 8,9,10,11,12,13,14,15 < 2^4 <= 2*n
h --> # of nodes < 2^h <= 2*n

if n < 2^n <= 2*n take lg and get
h <= lg(n) + 1 (where h is the minimum height of the tree to pack n nodes)
if our BST is tightly packed (balanced), we use lg(n) time

def - AVL tree, balance criteria of 1 node differing from each side.

mergesort
the merges of merge sort takes lgn, (the recursive steps)
combining the list in total takes n
so together they are nlgn

steps are operations that don't depend on the input size t(n)

"""


def binary_search(list_: list, value: int) -> bool:
    """ returns True if the item is in the list_"""

    l = len(list_)
    if l == 1:
        return list_[0] == value
    else:
        return (binary_search(list_[0:l // 2], value) or
                binary_search(list_[l // 2:len(list_)], value))


if __name__ == '__main__':
    d = [1, 3, 4, 201, 231, 2313, 1231541, 231515124]
    print(binary_search(d, 201))
    print(binary_search(d, 202))
