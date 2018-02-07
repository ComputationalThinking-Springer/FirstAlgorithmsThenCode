# Program INSERTION_SORT in Python
# Figure 5.2 from the book "Il Pensiero Computazionale: dagli algoritmi al coding"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Il Mulino


def insertion_sort(c):
    """
    Sort a vector c of n integers among which is defined a comparison relation.
    :param c: vector to be sorted
    """

    n = len(c)                                  # n is the number of elements of c

    for i in range(1, n):
        j = i
        while (j > 0) and (c[j - 1] > c[j]):
            tmp = c[j]                          # temporary variable
            c[j] = c[j - 1]                     # swaps c[j-1] with c[j]
            c[j - 1] = tmp
            j = j - 1


def main():

    c = [3, 10, 13, 5, 2, 31, 4, 1, 6, 20, 16, 15, 12, 40, 50, 42]

    print c

    insertion_sort(c)

    print c


if __name__ == "__main__":
    main()