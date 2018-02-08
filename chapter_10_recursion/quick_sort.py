# Program QUICK_SORT in Python
# Figure 10.12 from the book "Computational Thinking: First Algorithms, Then Code"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Springer


# loads mathematical functions
import numpy as np


def partition(c, p, q):
    """
    Rearrange a vector c in the portion between the indexes p and q, around a random selected pivot element.
    The elements lower than or equal to the pivot are moved to its left 
    whereas the elements greater than the pivot are moved to its right.
    :param c: vector to partition
    :param p: lower index of the part of the vector c to partition
    :param q: upper index of the part of the vector c to partition
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


def quick_sort(c, p, q):
    """
    Sort the vector c by using the function partition.
    :param c: vector to be sorted
    :param p: lower index of the part of the vector c to sort
    :param q: upper index of the part of the vector c to sort
    """

    if p < q:
        s = partition(c, p, q)
        quick_sort(c, p, s - 1)
        quick_sort(c, s + 1, q)


def main():
    c = [3, 10, 13, 5, 2, 31, 4, 1, 6, 20, 16, 15, 12, 40, 50, 42]

    print "\n Input vector to sort: ", c

    quick_sort(c, 0, len(c) - 1)

    print "\n Sorted vector: ", c


if __name__ == "__main__":
    main()
