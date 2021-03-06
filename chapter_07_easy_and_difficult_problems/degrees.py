# Program DEGREES in Python
# Figure 7.5 from the book "Computational Thinking: First Algorithms, Then Code"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Springer


# loads mathematical functions
import numpy as np


def degrees(M):
    """
    Program for parity checking of the degree of all the nodes in a graph with n nodes.
    :param M: matrix with dimension n x n
    :return: g output vector of the nodes' degree
    """

    n, n = M.shape
    g = [0] * n                             # output vector containing the node degrees

    for i in range(0, n):
        degree = 0                          # indicates the degree of node i
        for j in range(0, n):
            degree = degree + M[i, j]       # calculates the degree g of node i
        if degree % 2 == 1:
            print "The graph contains a node with odd degree"
            return g
        else:
            g[i] = degree

    print "All the nodes in the graph have even degree"

    return g


def main():

    M1 = np.asmatrix([
        [0, 1, 1, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 0]])

    degrees(M1)

    M2 = np.asmatrix([
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0]])

    degrees(M2)


if __name__ == "__main__":
    main()
