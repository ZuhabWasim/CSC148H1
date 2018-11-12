"""
Main module for the queue module.
"""
from csc148_queue import Queue


def list_queue(given_list: list, given_queue: Queue) -> None:
    """ Adds each element in given_list into given_queue and outputs in input order,
    every element and nested element from given_list in given_queue.
    """
    for item in given_list:
        given_queue.add(item)

    while not given_queue.is_empty():
        element = given_queue.remove()
        if not isinstance(element, list):
            print(element)
        else:
            for sub_item in element:
                given_queue.add(sub_item)


if __name__ == '__main__':
    # queue = Queue()
    # num = int(input('Please enter an integer: '))
    #
    # while num != 148:
    #     queue.add(num)
    #     num = int(input('Please enter an integer: '))
    #
    # sum = 0
    # while not queue.is_empty():
    #     sum += queue.remove()
    # print(str(sum))

    stck = Queue()
    # lst = [1, 3, 5]
    # list_queue(lst, stck)

    lst = [1, [3, 5], 7]
    list_queue(lst, stck)

    # lst = [1, [3, [5, 7], 9], 11]
    # list_queue(lst, stck)
