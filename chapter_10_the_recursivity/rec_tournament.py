# Program REC_TOURNAMENT in Python
# Figure 10.1 from the book "Il Pensiero Computazionale: dagli algoritmi al coding"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Il Mulino


# loads mathematical functions
import math


def rec_tournament(set, i, j):
    """
    Search the winner in a table using the recursion. 
    The participants are contained in a vector 'set' of n = 2^k elements, 
    but the program refers to a generic sub-tournament among the participants 
    contained in the portion set[i:j], inclusive.
    :param set: set of integers where to search the maximum on
    :param i: lower index of set
    :param j: upper index of set
    """

    if j == i + 1:                          # extreme situation with two player
        if set[i] > set[j]:
            return set[i]
        else:
            return set[j]

    m = int(math.floor((i + j) / 2))
    v1 = rec_tournament(set, i, m)          # v1 is the winner of the first sub-tournament
    v2 = rec_tournament(set, m + 1, j)      # v2 is the winner of the second sub-tournament

    if v1 > v2:
        return v1
    else:
        return v2


def main():

    set = [24, 15, 7, 9, 20, 49, 33, 35, 22, 40, 52, 12, 62, 30, 8, 43]

    print "the maximum is %d" % rec_tournament(set, 0, len(set) - 1)


if __name__ == "__main__":
    main()
