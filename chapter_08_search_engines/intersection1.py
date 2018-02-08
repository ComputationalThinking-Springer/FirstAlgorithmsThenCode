# Program INTERSECTION1 in Python
# Figure 8.5 from the book "Computational Thinking: First Algorithms, Then Code"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Springer


def intersection1(a, b):
    """
    Print all the elements of vector a which are contained in vector b.
    The search is performed by comparing each element of a with all the elements of b.
    The vectors can be unsorted because all the elements are sequentially examined and their equality is tested.
    :param a: vector a of n elements
    :param b: vector b of m elements
    """

    n = len(a)
    m = len(b)

    for i in range(0, n):
        for j in range(0, m):
            if a[i] == b[j]:
                print a[i]


def main():

    # the vectors are not sorted, on purpose
    pisa = [3, 9, 1, 200, 144]
    tower = [15, 9, 11, 101, 150, 21, 27, 500, 800, 89, 811]

    intersection1(tower, pisa)


if __name__ == "__main__":
    main()
