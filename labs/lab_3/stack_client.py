"""
The client for the stack module.
"""
from stack import Stack


def list_stack(given_list: list, given_stack: Stack) -> None:
    """ Adds each element in given_list into given_stack and outputs in reverse order,
    every element and nested element from given_list in given_stack.
    """
    for item in given_list:
        given_stack.add(item)

    while not given_stack.is_empty():
        element = given_stack.remove()
        if not isinstance(element, list):
            print(element)
        else:
            for sub_item in element:
                given_stack.add(sub_item)

if __name__ == '__main__':
    # stack = stack.Stack()
    # st = input('Type a string: ')
    # while st != 'end':
    #     stack.add(st)
    #     st = input('Type a string: ')
    #
    # while not stack.is_empty():
    #     print(stack.remove())

    stck = Stack()
    lst = [1, 3, 5]
    list_stack(lst, stck)

    lst = [1, [3, 5], 7]
    list_stack(lst, stck)

    lst = [1, [3, [5, 7], 9], 11]
    list_stack(lst, stck)
