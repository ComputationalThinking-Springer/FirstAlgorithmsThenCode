# Program PARTITION in Python
# Figure 10.9 from the book "Il Pensiero Computazionale: dagli algoritmi al coding"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Il Mulino


# loads mathematical functions
import numpy as np


def partition(c, p, q):
    """
    Rearrange a vector c in the portion between the indexes p and q, around a random selected pivot element.
    The elements lower than or equals to the pivot are moved to its left 
    and the elements greater are moved to its right.
    :param c: vector to partition
    :param p: lower index of vector c
    :param q: upper index of vector c
    """

    r = np.random.randint(p, q + 1)

    c[r], c[q] = c[q], c[r]                 # now the pivot is in c[q]

    i = p - 1
    for j in range(p, q):
        if c[j] <= c[q]:
            i = i + 1
            if i < j:
                c[i], c[j] = c[j], c[i]

    s = i + 1                               # pivot final position
    c[q], c[s] = c[s], c[q]                 # now the pivot is in c[s]
    return s


def main():

    c = [3, 10, 13, 5, 2, 31, 4, 1, 6, 20, 16, 15, 12, 40, 50, 42]

    print "\n Input vector to partition: ", c

    cc = partition(c, 0, len(c) - 1)

    print "\n Partitioned vector (pivot in position %d): " % cc, c


if __name__ == "__main__":
    main()
