# Program TOURNAMENT in Python
# Figure 3.4 from the book "Computational Thinking: First Algorithms, Then Code"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Springer


# loads mathematical functions
import math


def tournament(set):
    """
    Search the maximum in a table with n = 2^k partecipants.
    :param set: set of integers on which to seek the maximum
    """

    n = len(set)                        # n is the number of elements of set
    k = int(math.log(n, 2))             # leaves level

    p = list()
    for i in range(0, n):               # copy set in p
        p.append(set[i])

    h = k                               # h is the current level
    while h >= 1:                       # runs the matches at level h, from k to 1
        i = 0
        v = list()
                                        # x**y is the python expression for x^y
        while i <= 2**h - 2:            # carica in v i vincitori
            if p[i] > p[i + 1]:         # p[i] e' il vincitore
                v.append(p[i])
            else:                       # p[i+1] e' il vincitore
                v.append(p[i + 1])
            i = i + 2

        for i in range(0, 2**(h-1)):    # trasferisce in p i vincitori
            p[i] = v[i]

        h = h - 1                       # si sposta al livello superiore

    print "il massimo e' %d" % p[0]


def main():

    set = [24, 15, 7, 9, 20, 49, 33, 35, 22, 40, 52, 12, 62, 30, 8, 43]

    tournament(set)


if __name__ == "__main__":
    main()
