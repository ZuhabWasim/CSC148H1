"""
The number of ways you can make n cent postage stamps using 3,4,5 cent stamps
"""

seen = {}


def postage(n: int):
    """ Number of ways for n
    n = 3i + 4j + 5k
    """
    ways = []
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if n == 3 * i + 4 * j + 5 * k and (i, j, k) not in ways:
                    ways.append((i, j, k))
                    count += 1
    # return ways
    return count

def recp(n: int):
    """ Number of ways for n
    n = 3i + 4j + 5k
    """
    if n <= 2:
        return 0
    elif n <= 7:
        return 1
    else:
        if n % 5 == 0:
            c = 1
        else:
            c = 0
        return recp(n-3) + recp(n-4) - recp(n-7) + c


if __name__ == "__main__":
    # print("n p(n) a(n)")
    for n in range(5, 51):
        pn = postage(n)
        # myn = 2*postage(n-3) + postage(n-4) - 2*postage(n-5)
        # fn = postage(n-3) + postage(n-4) - postage(n-7)
        # myn2 = 4*postage(n-3) -3*postage(n-4)
        # myn2 = postage(n-3) + postage(n-5) - 2*postage(n-4)
        print(n, pn, recp(n))
        # pn = postage(n)
        #
        # # Past values
        # pn3 = postage(n - 3)
        # pn4 = postage(n - 4)
        # pn5 = postage(n - 5)
        #
        # # Error from correct
        # errp3 = pn - pn3
        # errp4 = pn - pn4
        # errp5 = pn - pn5
        #
        # # Difference of error
        # err2p4 = errp3 - errp4
        # err2p5 = errp4 - errp5
        # print("       n: " + str(n),
        #       "    p(n): " + str(pn),
        #       "    p(n-3): " + str(pn3),
        #       "    p(n-4): " + str(pn4),
        #       "    p(n-5): " + str(pn5),
        #       "    p(er3): " + str(errp3),
        #       "    p(er4): " + str(errp4),
        #       "    p(er5): " + str(errp5),
        #       "    p(2n4): " + str(err2p4),
        #       "    p(2n5): " + str(err2p5))
        # print(n, recp(n), len(postage(n)))
        # print(n, len(postage(n)))
    print(postage(18))
