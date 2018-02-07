# Program MS_RIC in Python
# Figure 10.14 from the book "Il Pensiero Computazionale: dagli algoritmi al coding"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Il Mulino


# loads mathematical functions
import math


def fusion(a, b):
    """
    Merges two sorted sequences a and b in a sorted sequence f.
    :param a: sorted sequence
    :param b: sorted sequence
    :return: f is the sorted vector contationing all the elements of a join b.
    """

    m = len(a)                  # m is the number of elements of a and b

    f = [None] * (m + m)        # initializes the auxiliary vector f
    i = j = k = 0

    while (i < m) and (j < m):
        if a[i] <= b[j]:        # the minimum is a[i]
            f[k] = a[i]
            i = i + 1
        else:
            f[k] = b[j]
            j = j + 1
        k = k + 1

    while i < m:
        f[k] = a[i]
        i = i + 1
        k = k + 1

    while j < m:
        f[k] = b[j]
        j = j + 1
        k = k + 1

    return f


def ms_ric(c, i, j):
    """
    Recoursive version of the merge sort of a vector c of n = 2^h elements.
    The program is written to sort a generic sub-vector c[i:j], inclusive
    :param c: vector to sort
    :param i: lower index of vector c
    :param j: upper index of vector c
    """

    if i < j:
        m = int(math.floor((i + j) / 2))
        ms_ric(c, i, m)
        ms_ric(c, m + 1, j)
        f = fusion(c[i:m + 1], c[m + 1:j + 1])
        c[i:j + 1] = f                                # mov to c some elements of f


def main():
    c = [3, 10, 13, 5, 2, 31, 4, 1, 6, 20, 16, 15, 12, 40, 50, 42]

    print "\n Input sequence to sort: ", c

    ms_ric(c, 0, len(c))

    print "\n Sorted sequence: ", c


if __name__ == "__main__":
    main()
