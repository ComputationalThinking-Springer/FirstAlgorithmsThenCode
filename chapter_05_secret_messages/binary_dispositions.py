# Program BINARY_DISPOSITIONS in Python
# Figure 5.6 from the book "Computational Thinking: First Algorithms, Then Code"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Springer


def binary_dispositions(n):
    """
    Program for constructing and printing all the binary dispositions of n bit 
    in a vector v, for binary growing numbers.
    :param n: number of bits of the vector
    """

    v = [0] * n
    print v[::-1]           # prints the first disposition 00...0

    i = 0
    while i <= n - 1:
        if v[i] == 0:       # for i > 0, we have v[j] = 0 for j < i
            v[i] = 1
            print v[::-1]   # print the last disposition built
            i = 0           # move back to the least meaningful bit
        else:
            v[i] = 0        # the bit 1 in position i is changed to 0
            i = i + 1       # moves to the next bit


def main():

    binary_dispositions(4)


if __name__ == "__main__":
    main()
