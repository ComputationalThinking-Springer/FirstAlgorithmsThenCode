# Program MAXIMUM in Python
# Figure 3.2 from the book "Il Pensiero Computazionale: dagli algoritmi al coding"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Il Mulino


def counting_sort(c, k):
    """
    Sort a vector c of n integers greater than or equal to 0 and lower than k 
    among which is defined the comparison relation <= 
    using an auxiliary vector of k positions.
    :param c: vector to be sorted
    """

    n = len(c)                                  # n is the number of elements of c

    a = [0] * k                                 # intialize the auxliary vector a of k positions

    for i in range(0, n):
        a[c[i]] = a[c[i]] + 1

    h = 0
    for j in range(0, k):
        for i in range(0, a[j]):
            c[h] = j
            h += 1


def main():

    c = [3, 2, 3, 3, 3]
    k = 4

    print c

    counting_sort(c, k)

    print c


if __name__ == "__main__":
    main()
