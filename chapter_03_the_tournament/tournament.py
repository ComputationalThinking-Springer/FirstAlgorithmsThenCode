# Program TOURNAMENT in Python
# Figure 3.4 from the book "Computational Thinking: First Algorithms, Then Code"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Springer


# loads mathematical functions
import math


def tournament(set):
    """
    Search the maximum in a table with n = 2^k partecipants.
    :param set: set of integers in which to search for the maximum
    """

    n = len(set)                        # n is the number of elements of set
    k = int(math.log(n, 2))             # level of the leaves 

    p = list()
    for i in range(0, n):               # copy the set in p
        p.append(set[i])

    h = k                               # h is the current level
    while h >= 1:                       # runs the matches at level h, from k to 1
        i = 0
        v = list()
                                        # x**y is the python expression for x^y
        while i <= 2**h - 2:            # load in v the winners
            if p[i] > p[i + 1]:         # p[i] is the winner
                v.append(p[i])
            else:                       # p[i+1] is the winner
                v.append(p[i + 1])
            i = i + 2

        for i in range(0, 2**(h-1)):    # copies in p the winners
            p[i] = v[i]

        h = h - 1                       # moves to the level above

    print "the maximum is %d" % p[0]


def main():

    set = [24, 15, 7, 9, 20, 49, 33, 35, 22, 40, 52, 12, 62, 30, 8, 43]

    tournament(set)


if __name__ == "__main__":
    main()
