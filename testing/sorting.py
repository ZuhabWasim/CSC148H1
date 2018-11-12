"""
Question 5's implementation of shade_sort with the extension of yellow.
"""

from typing import List


def four_shade_sort(colour_list: List[str]) -> None:
    """ Put colour_list in order "b" < "g" < "r".

    precondition: colour_list is a List[str] from {"b", "g", "r"}

    >>> list_ = ["r", "b", "g", "y"]
    >>> four_shade_sort(list_)
    >>> list_ == ["b", "g", "r", "y"]
    True

    postcondition: colour_list has same strings as before, ordered "b" < "g" < "r" < "y"
    """
    # TODO: initialize blue, green, red to be consistent with loop invariants.
    blue, green, red, yellow = 0, 0, 0, len(colour_list)
    # Hint: blue, green may increase while red decreases.
    #
    # loop invariants:
    #
    # 0 <= blue <= green <= red <= yellow <= len(colour_list)
    # colour_list[0 : green] + colour_list[yellow :] same colours as before (possibly permuted)
    # and all([c == "b" for c in colour_list[0 : blue]])
    # and all([c == "g" for c in colour_list[blue : green]])
    # and all([c == "r" for c in colour_list[green : red]])
    # and all([c == "y" for c in colour_list[yellow :]])
    #
    # TODO: implement loop using invariants above!
    i = 0

    while red < yellow:  # Once red is equal to yellow,  then the list_ must be completely sorted
        if colour_list[i] == "b":
            colour_list.insert(0, colour_list.pop(i))
            blue += 1
            green += 1
            red += 1
            i += 1
        elif colour_list[i] == "g":
            colour_list.insert(green, colour_list.pop(i))
            green += 1
            red += 1
            i += 1
        elif colour_list[i] == "r":
            colour_list.insert(red, colour_list.pop(i))
            red += 1
            i += 1
        elif colour_list[i] == "y":
            colour_list.append(colour_list.pop(i))
            yellow -= 1
            i += 0

        # Invariant checking

        # Should contain the same elements as before, plus some more (maybe permutated)
        # print(colour_list[0: green] + colour_list[red:])

        # Checks if each sub slice should be sorted in its own no matter the iteration.
        # print(all([c == "b" for c in colour_list[0: blue]])
        #       and all([c == "g" for c in colour_list[blue: green]])
        #       and all([c == "r" for c in colour_list[green: red]])
        #       and all([c == "y" for c in colour_list[yellow:]]))

        # Checks the current values of blue, green, red,
        # print("Current pass i = " + str(i) + " :", blue, green, red, "Current state: " + str(colour_list_))
        # print("blue: ", colour_list[0:blue],
        #       "  green: ", colour_list[blue:green],
        #       "  red: ", colour_list[green:red],
        #       "  yellow: ", colour_list[yellow:])


def shade_sort(colour_list: List[str]) -> None:
    """ Put colour_list in order "b" < "g" < "r".

    precondition: colour_list is a List[str] from {"b", "g", "r"}

    >>> list_ = ["r", "b", "g"]
    >>> shade_sort(list_)
    >>> list_ == ["b", "g", "r"]
    True

    postcondition: colour_list has same strings as before, ordered "b" < "g" < "r"
    """
    # TODO: initialize blue, green, red to be consistent with loop invariants.
    blue, green, red = 0, 0, len(colour_list)
    # Hint: blue, green may increase while red decreases.
    #
    # loop invariants:
    #
    # 0 <= blue <= green <= red <= len(colour_list)
    # colour_list[0 : green] + colour_list[red :] same colours as before (possibly permuted)
    # and all([c == "b" for c in colour_list[0 : blue]])
    # and all([c == "g" for c in colour_list[blue : green]])
    # and all([c == "r" for c in colour_list[red :]])
    #
    # TODO: implement loop using invariants above!
    i = 0

    while green < red:  # Once green is equal to red,  then the list_ must be completely sorted
        if colour_list[i] == "b":
            colour_list.insert(0, colour_list.pop(i))
            blue += 1
            green += 1
            i += 1
        elif colour_list[i] == "g":
            green += 1
            i += 1
        elif colour_list[i] == "r":
            colour_list.append(colour_list.pop(i))
            red -= 1
            i += 0

if __name__ == "__main__":
    colour_list_ = ["r", "b", "y", "r", "y", "b", "b", "g", "y", "r", "y", "g", "g", "y", "r", "b", "r", "b", "g", "y"]
    four_shade_sort(colour_list_)
    print(colour_list_)
    #
    print("")
    print("")
    list_ = ["r", "b", "g", "y"]
    four_shade_sort(list_)
    print(list_)
