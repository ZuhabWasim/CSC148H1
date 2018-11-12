def merge(L1, L2):
    """return merge of L1 and L2
    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([1, 2, 3], [0, 4, 5])
    [0, 1, 2, 3, 4, 5]
    >>> merge([0], [1, 2, 3, 4])
    [0, 1, 2, 3, 4]
    """
    L = []
    i1, i2 = 0, 0
    while i1 < len(L1) and i2 < len(L2):
        if L1[i1] < L2[i2]:
            L.append(L1[i1])
            i1 += 1
        else:
            L.append(L2[i2])
            i2 += 1
    return L + L1[i1:] + L2[i2:]


def merge_sort(L):
    """Produce copy of L in non-decreasing order
    >>> merge_sort([1, 5, 3, 4, 2])
    [1, 2, 3, 4, 5]
    >>> L = list(range(20))
    >>> shuffle(L)
    >>> merge_sort(L) == list(range(20))
    True
    """
    if len(L) < 2:
        return L[:]
    else:
        return merge(merge_sort(L[: len(L) // 2]),
                     merge_sort(L[len(L) // 2 :]))
if __name__ == "__main__":
    import doctest
    doctest.testmod()
