# Program INTERSECTION1 in Python
# Figure 8.5 from the book "Il Pensiero Computazionale: dagli algoritmi al coding"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Il Mulino


def intersection1(a, b):
    """
    Prints all the elements of vector a which are contained also in vector b.
    The search is performed by comparing each element of a with all the elements of b.
    The vectors can be not sorted because all the elements are sequentially examined and their equality is tested.
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

    # the vectors are not sorted out of purpose
    pisa = [3, 9, 1, 200, 144]
    tower = [15, 9, 11, 101, 150, 21, 27, 500, 800, 89, 811]

    intersection1(tower, pisa)


if __name__ == "__main__":
    main()
