""" Lecture 4 Notes

Linked lists are are lists that allocate just enough memory an avoids over usage.

regular lists access indeices by retrieving all the conticuous memory spaces that can
get increasingly uneccessary as time goes on.

nodes are referenced and linked together to access the next nodes, rather than index values
these nodes can be anywhere in memory and does not have to be grouped all together as regular lists are.

If you wanted to find the middle of the linked list, you cannot calculate it from just knowing the begginning
of the list.
However with linked lists, you can access individual values alot faster than a from a list.

Think of linked lists in two different ways
1. as lists made up of an item (value) and a sub-list (rest)
    - implemented using recursion
    - but python does not support recursion very well (loses stack space after 1000 nodes)
    - not really required atm for jobs

    - identifying the list with the first node
    - that first node contains the rest of the list and so on
    - first nestation is the first node, second nestation is the second node and so on

2. as objects (nodes) with a value and a reference to other similar objects
    - represented as nodes pointing to other nodes and finally pointing to an end
    - one class to represent nodes
    - another class to represent the list it self, the (wrapper) to represent the linked list
    as a whole.

next_ : Union["LinkedListNode", None] = None
Union means it could either be of type LinkedListNode or NoneType

note: when you make an attribute that has the same name as a python already defined name, it would
'shadow' the python expression so to avoid this we use '_' at the end to differ.


LinkedLists contain a __str__ and __eq__ methods and normally
    - __eq__ would be defined as the three types
        id1 == id2
        value1 == value2
        value1 == value2 and next1 == next2

walking on a list
    Make a reference to (at least one) node, and move it along the
    list:

    cur_node = self.front
    while <some condition here...>:
        # do something here...
        cur_node = cur_node.nxt

    'while current_node is not None:' the 'is not None' is not needed but you should have it incase
    you don't know what the if the value of current_node is either empty, a value, or something else.

__contains__ built in method of 'in'
    cur_node = self.front
    while >some condition here...>:
        #do something here # return True
        cur_node = cur_node.nxt
    return False

__getitem__
    enables things like
    print(lnk[0])
    print(lnk[0:3])
    remember that for a list of size n, the indices up to n - 1 and dont to -(n)

for the append function
    we need to change:
        - last node
        - former last node
        - back
        - size
        - possibly front

if you wanted to implement a queue using linked lists, there exists an assymtry between the direction
    of retrieval being at the front or back.
    If the back one is removed, the back of the linked list would still need to iterate through self.size - 1
    to find the next one.
    i.e. we need to nd the second last node. Walk two references along
    the list.
        prev_node, cur_node = None, lnk.front
        # walk along until cur_node is lnk.back
        while <some condition>:
            prev_node = cur_node
            cur_node = cur_node.nxt
"""
