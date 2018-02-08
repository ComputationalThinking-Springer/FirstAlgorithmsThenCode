# Program MERGE in Python
# Figure 6.4 from the book "Computational Thinking: First Algorithms, Then Code"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Springer


def fusion(a, b):
    """
    Merges two sorted sequences a and b in a sorted sequence f.
    :param a: sorted sequence
    :param b: sorted sequence
    :return: f is the sorted vector contationing all the elements of a join b.
    """

    m = len(a)                  # m is the number of elements of a and b

    f = [None] * (m + m)        # initializes the auxiliary vector f
    i = j = k = 0

    while (i < m) and (j < m):
        if a[i] <= b[j]:        # the minimum is a[i]
            f[k] = a[i]
            i = i + 1
        else:
            f[k] = b[j]
            j = j + 1
        k = k + 1

    while i < m:
        f[k] = a[i]
        i = i + 1
        k = k + 1

    while j < m:
        f[k] = b[j]
        j = j + 1
        k = k + 1

    return f


def main():

    a = [1, 5, 7]
    b = [2, 3, 4]

    print a, b

    f = fusion(a, b)

    print f


if __name__ == "__main__":
    main()
