""" classes LinkedListNode and LinkedList
"""
from typing import Union, Any


class LinkedListNode:
    """
    Node to be used in linked list

    === Attributes ===
    next_ - successor to this LinkedListNode
    value - data represented by this LinkedListNode
    """
    next_: Union["LinkedListNode", None]

    def __init__(self, value: object,
                 next_: Union["LinkedListNode", None]=None) -> None:
        """
        Create LinkedListNode self with data value and successor next

        >>> LinkedListNode(5).value
        5
        >>> LinkedListNode(5).next_ is None
        True
        """

        self.value, self.next_ = value, next_

    def __str__(self) -> str:
        """
        Return a user-friendly representation of this LinkedListNode.

        >>> n = LinkedListNode(5, LinkedListNode(7))
        >>> print(n)
        5 -> 7 ->|

        s = "{} ->".format(self.value)

        current_node = self.next
        while current_node is not None:

        """

        s = "{} ->".format(self.value)  # start with a string s to represent current node.

        current_node = self.next_  # create a reference to "walk" along the list
        while current_node is not None:  # for each subsequent node in the list,
            #  build s
            s += " {} ->".format(current_node.value)
            current_node = current_node.next_
        # add "|" at the end of the list
        s += '|'
        return s

    def __eq__(self, other: Any) -> bool:
        """
        Return whether LinkedListNode self is equivalent to other.

        >>> LinkedListNode(5).__eq__(5)
        False
        >>> n1 = LinkedListNode(5, LinkedListNode(7))
        >>> n2 = LinkedListNode(5, LinkedListNode(7, None))
        >>> n1.__eq__(n2)
        True
        """

        if type(self) == type(other):
            is_equal = (self.value == other.value)
            current_node = self.next_
            other_node = other.next_
            while (current_node is not None) and (other_node is not None) and is_equal:
                is_equal = (current_node.value == other_node.value)
                current_node = self.next_
                other_node = other.next_
            return is_equal
        else:
            return False


class LinkedList:  # The 'wrapper' to collect all the nodes.
    """
    Collection of LinkedListNodes

    === Attributes ==
    front - first node of this LinkedList
    back - last node of this LinkedList
    size - number of nodes in this LinkedList, >= 0
    """
    front: Union[LinkedListNode, None]
    back: Union[LinkedListNode, None]
    size: int

    def __init__(self) -> None:
        """
        Create an empty linked list.
        """
        self.front, self.back, self.size = None, None, 0

    def __str__(self) -> str:
        """
        Return a human-friendly string representation of
        LinkedList self.

        >>> lnk = LinkedList()
        >>> lnk.front = LinkedListNode(5)
        >>> lnk.back = lnk.front
        >>> print(lnk)
        5 ->|
        """
        pass

    def __eq__(self, other: Any) -> bool:
        """
        Return whether LinkedList self is equivalent to
        other.

        >>> LinkedList().__eq__(None)
        False
        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(5)
        >>> lnk.__eq__(lnk2)
        True
        """
        pass

    def append(self, value: object) -> None:
        """
        Insert a new LinkedListNode with value after self.back.

        >>> lnk = LinkedList()
        >>> lnk.append(5)
        >>> lnk.size
        1
        >>> print(lnk.front)
        5 ->|
        >>> lnk.append(6)
        >>> lnk.size
        2
        >>> print(lnk.front)
        5 -> 6 ->|
        """
        # create the new node
        new_node = LinkedListNode(value)
        # if the list is not empty, front is the same
        if self.back is not None:
            self.back.next_ = new_node
            self.back = new_node
        else:
            # If the list is empty, new_node is the new front and back.
            self.front = new_node
            self.back = new_node
        # increase the size.
        self.size += 1

    def prepend(self, value: object) -> None:
        """
        Insert value before LinkedList self.front.

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> str(lnk.front)
        '2 -> 1 -> 0 ->|'
        >>> lnk.size
        3
        """
        # mine
        # self.front = LinkedListNode(value, self.front)
        # self.size += 1

        # Create a new node with next_referring to front
        new_node = LinkedListNode(value, self.front)
        # Change front
        self.front = new_node
        # if the list was empty, change back
        if self.back is None:
            self.back = new_node
        # update size
        self.size += 1

    def pop_front(self):
        """
        Remove self.front and return its value. Assume
        self.size >= 1
        """
        saved_value = self.front.value
        self.delete_front()
        return saved_value

    def delete_back(self) -> None:
        """
        """
        previous_node, current_node = None, self.front
        # walk along until your current node is the back
        while current_node != self.back:
            previous_node = current_node
            current_node = current_node.next_
        return previous_node

    def delete_front(self) -> None:
        """
        Delete LinkedListNode self.front from self.

        Assume self.front is not None

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.delete_front()
        >>> str(lnk.front)
        '1 -> 0 ->|'
        >>> lnk.size
        2
        >>> lnk.delete_front()
        >>> lnk.delete_front()
        >>> str(lnk.front)
        'None'
        """

        if self.size == 1:
            self.back = self.front = None
        else:
            self.front = self.front.next_
        self.size -= 1

    def __getitem__(self, index: int) -> object:
        """
        Return the value at LinkedList self's position index,
        which must be a valid position in LinkedList self.

        >>> lnk = LinkedList()
        >>> lnk.prepend(1)
        >>> lnk.prepend(0)
        >>> lnk.__getitem__(1)
        1
        >>> lnk[-1]
        1
        """
        # Wether index is out of range
        if index >= self.size or index < self.size * -1:
            raise IndexError('The index {} is out of range.'.format(index))
        elif index < 0:
            index += self.size
        else:
            pass
        current_node = self.front
        for steps in range(index):
            current_node  = current_node.next_
        return current_node.value

    def __contains__(self, value: object) -> bool:
        """
        Return whether LinkedList self contains value.

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.__contains__(1)
        True
        >>> lnk.__contains__(3)
        False
        """
        current_node = self.front
        # "walk" the linked list
        while current_node is not None:
            # if any node has a value, return True
            if current_node.value == value:
                return True
            current_node = current_node.next_
        # The value is not in the linked list
        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
