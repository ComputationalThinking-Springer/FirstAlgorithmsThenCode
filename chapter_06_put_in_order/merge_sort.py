# Program MERGE_SORT in Python
# Figure 6.6 from the book "Computational Thinking: First Algorithms, Then Code"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Springer


# loads mathematical functions
import math


def merge_sort(c):
    """
    Sorts a vector c of n = 2^h integer among which is defined a comparison relation <=. 
    It uses the structur of the fusion program.
    :param c: vector to be sorted
    """

    n = len(c)                  # n is the number of elements of c

    h = int(math.log(n, 2))

    f = [None] * n              # intialize the auxliary vector f

    for r in range(1, h+1):
        for s in range(0, 2**(h-r)):
            a = 2**r * s
            b = a + 2**(r-1)
            i = a
            j = b
            k = a

            while (i < a + 2**(r-1)) and (j < b + 2**(r-1)):
                if c[i] <= c[j]:
                    f[k] = c[i]
                    i = i + 1
                else:
                    f[k] = c[j]
                    j = j + 1
                k = k + 1

            while i < a + 2**(r-1):
                f[k] = c[i]
                i = i + 1
                k = k + 1

            while j < b + 2**(r-1):
                f[k] = c[j]
                j = j + 1
                k = k + 1

            for k in range(0, a + 2**r):
                c[k] = f[k]


def main():
    c = [3, 10, 13, 5, 2, 31, 4, 1, 6, 20, 16, 15, 12, 40, 50, 42]

    print c

    merge_sort(c)

    print c


if __name__ == "__main__":
    main()
