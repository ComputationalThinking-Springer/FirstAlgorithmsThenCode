# Program MATRIX_PRODUCT in Python
# Figure 7.3 from the book "Computational Thinking: First Algorithms, Then Code"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Springer


# loads mathematical functions
import numpy as np


def matrix_product(A, B):
    """
    Program to calculate the product of two matrices.
    :param A: matrix with dimension m x n
    :param B: matrix with dimension n x p
    :return: C = A x B matrix with dimension m x p
    """

    m, n = A.shape
    n, p = B.shape
    C = np.zeros((m, p))

    for i in range(0, m):
        for j in range(0, p):
            s = 0
            for k in range(0, n):
                s = s + A[i, k] * B[k, j]
            C[i, j] = s

    return C


def main():

    K = np.asmatrix([
        [0, 2, 2, 1],
        [2, 0, 0, 1],
        [2, 0, 0, 1],
        [1, 1, 1, 0]])

    K2 = matrix_product(K, K)

    print K2


if __name__ == "__main__":
    main()
