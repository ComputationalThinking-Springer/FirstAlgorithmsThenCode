# Program INTERSECTION3 in Python
# Figure 8.7 from the book "Computational Thinking: First Algorithms, Then Code"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Springer


def intersection3(a, b):
    """
    Prints all the elements of vector a which are contained also in vector b.
    Both vectors must be sorted.
    It si faster than INTERSECTION1 and INTERSECTION2.
    :param a: sorted vector a of n elements
    :param b: sorted vector b of m elements
    """

    n = len(a)
    m = len(b)

    i = 0
    j = 0

    while (i < n) and (j < m):
        if a[i] < b[j]:
            i = i + 1
        elif b[j] < a[i]:
            j = j + 1
        else:
            print a[i]          # indeed a[i] = b[j]
            i = i + 1
            j = j + 1


def main():

    # both vectors are sorted
    pisa = [1, 3, 9, 144, 210]
    tower = [9, 11, 15, 21, 27, 89, 144, 150, 500, 800, 811]

    intersection3(tower, pisa)


if __name__ == "__main__":
    main()
