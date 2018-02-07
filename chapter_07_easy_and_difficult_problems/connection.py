# Program CONNECTION in Python
# Figure 7.4 from the book "Il Pensiero Computazionale: dagli algoritmi al coding"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Il Mulino


# loads mathematical functions
import numpy as np


def connection(M):
    """
    Program to check if a graph with n nodes described by matrix M, is connected 
    through a breadth-first search.
    :param M: matrix with dimension n x n
    """

    n, n = M.shape
    r = [0] * n                       # vector of n cells to store the nodes reachable from 0

    r[0] = 0
    s = 0
    f = 0
    while s <= f:                     # f indicates the last cell occupied by r
        i = r[s]                      # indicates the node examinded
        for j in range(1, n):
            if M[i, j] > 0:           # that is for each element > 0 at row i
                if j not in r[0: f]:
                    f = f + 1
                    r[f] = j
                    if f == n - 1:
                        print "the graph is connected"
                        return

        s = s + 1

    print "the graph is not connected"


def main():

    # The graph must be indirected and consequently
    # the matrices M1 e M2 must be symmetric

    M1 = np.asmatrix([
        [0, 1, 1, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 0]])

    connection(M1)

    M2 = np.asmatrix([
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]])

    connection(M2)


if __name__ == "__main__":
    main()
