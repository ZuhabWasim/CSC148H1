""" Yeet yaw
"""
# count subsequences
from typing import Union

"""
AAAAA
AAA__ : __AAA
AA_A_ : _A_AA
A_AA_ : _AA_A
_AAA_ : 
AA__A : A__AA
A_A_A : 
"""


def count_subsequences(s1: str, s2: str,
                       i: int, j: int) -> int:
    """ Return the number of times s1[: i] occurs as a
    subsequence of s2[: j].

    Precondition: 0 <= i <= len(s1), 0 <= j <= len(s2)

    >>> count_subsequences("", "Danny", 0, 5)
    1
    >>> count_subsequences("Danny", "", 5, 0)
    0
    >>> count_subsequences("AAA", "AAAAA", 3, 5)
    10

    Postcondition: returns number of times s1[: i} occurs as a
    subsequence of s2[: j]
    """
    if i == 0:
        # print("return 1")
        return 1
    elif i > j:
        # print("return 0")
        return 0
    elif s1[i-1] != s2[j-1]:
        # print("1:Since " + str(s1[:i-1]) + " != " + str(s2[:j-1]) +
        #       ", we call " + str(s1[:i]) + " and " + str(s2[:j-1]))
        return count_subsequences(s1, s2, i, j-1)
    else:  # s1[i-1] == s2[j-1]
        # print("2:Since " + str(s1[:i - 1]) + " == " + str(s2[:j - 1]) +
        #       ", we call " + str(s1[:i]) + "," + str(s2[:j - 1]) + " and " + str(s1[:i-1]) + "," + str(s2[:j - 1]))
        return (count_subsequences(s1, s2, i, j-1)
                + count_subsequences(s1, s2, i-1, j-1))


def count_subsequences_memoized(s1: str, s2: str, i: int, j: int,
                                seen: Union[dict, None]=None) -> int:
    """ Return the number of times s1[: i] occurs as a
    subsequence of s2[: j].

    Precondition: 0 <= i < len(s1), 0 <= j < len(s2)

    >>> count_subsequences_memoized("", "Danny", 0, 5, None)
    1
    >>> count_subsequences_memoized("Danny", "", 5, 0, None)
    0
    >>> count_subsequences_memoized("AAA", "AAAAA", 3, 5, None)
    10

    Postcondition: returns number of times s1[: i} occurs as a
    subsequence of s2[: j]
    """
    if seen is None:
        seen = {}
    else:
        pass
    if (i, j) not in seen:
        if i == 0:
            seen[(i, j)] = 1
        elif i > j:
            seen[(i, j)] = 0
        elif s1[i-1] != s2[j-1]:
            seen[(i, j)] = count_subsequences_memoized(s1, s2, i, j-1, seen)
        else:
            seen[(i, j)] = (count_subsequences_memoized(s1, s2, i, j-1, seen)
                            + count_subsequences_memoized(s1, s2, i-1, j-1, seen))
    return seen[(i, j)]


if __name__ == "__main__":
    # st1 = "TAGAC"
    # st2 = "ATAGGACCA"
    # print(count_subsequences(st1, st2, len(st1), len(st2)))
    #
    # st1 = "zuhab"
    # st2 = "zuhabzzhuzhabahzuzhuabzbzbzuhab"
    # print(count_subsequences(st1, st2, len(st1), len(st2)))
    #
    # st1 = "apple"
    # st2 = "aapppllee"
    # print(count_subsequences(st1, st2, len(st1), len(st2)))
    st = ''
    for j in range(10):
        st = ''
        for i in range(1,j+1):
            st += str(count_subsequences("A" * i, "A" * j, len("A" * i), len("A" * j))) + " "
            print(st)
