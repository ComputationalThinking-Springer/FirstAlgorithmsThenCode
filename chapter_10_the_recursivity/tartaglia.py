# Program TARTAGLIA in Python
# Figure 10.13 from the book "Il Pensiero Computazionale: dagli algoritmi al coding"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Il Mulino


# loads mathematical functions
import numpy as np


def tartaglia(n):
    """
    Build the Tartaglia's Triangle up to row n.
    :param n: rows in the Tartaglia's Triangle to build
    """

    T = np.zeros((n, n))

    for i in range(0, n):
        T[i, 0] = 1
        T[i, i] = 1

    for i in range(2, n):
        for j in range(1, i):
            T[i, j] = T[i - 1, j] + T[i - 1, j - 1]

    return T


def main():

    T = tartaglia(8)

    print T


if __name__ == "__main__":
    main()
