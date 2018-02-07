# Program in Python whcih include BWT_INVERSE and other programs allowing to calculate BWT_DIRECT and
# to print intermediate results
# Figure 9.8 from the book "Il Pensiero Computazionale: dagli algoritmi al coding"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Il Mulino


# loads mathematical functions
import numpy as np


def bwt_direct(t):
    """
    Burrows-Wheeler algorithm for the permutation of a text t into a string l.
    :param t: text to be transformed
    :return: l last, and f first, column of matrix M built starting from t
    """

    line = t + '#'                          # adds a special character

    M_str = list()                          # creates the matrix with all the rotations
    print "\n\nUnsorted matrix M"

    for i in range(0, len(line)):
        new_line = line[i:] + line[:i]
        print " ", new_line
        M_str.append(line[i:] + line[:i])

    M = list()
    M_str = sorted(M_str)                   # sorts the matrix

    print "\n\nAlphabetically sorted matrix M"

    for i in range(0, len(line)):
        print " ", M_str[i]

    for i in range(0, len(line)):
        M.append(list(M_str[i]))

    M = np.asmatrix(M)

    l = M[:, -1].tostring()                 # extracts the last column
    f = M[:, 0].tostring()                  # extracts the first column

    return l, f


def set_first_occurence(s, f):
    """
    Returns the postition in f of the first occurrence of the symbol s.
    :param s: symbol to search for
    :param f: string where to search on
    :return: position in f of the first occurrence of the character s
    """

    for i in range(0, len(f)):
        if f[i] == s:
            return i

    return -1


def rank(l, r):
    """
    Calculates the number of times tha letter l[r] appears in the prefix l[0:r-1].
    :param l: last column of matrix M alphabetically sorted
    :param r: iindex of the symbol for rank calculus
    :return: number of times tha letter l[r] appears in the prefix l[0:r-1]
    """

    conut = 0
    for i in range(0, r):
        if l[i] == l[r]:
            conut += 1

    return conut


def bwt_inverse(l, f):
    """
    Algorithm that inversts the Burrows-Wheeler transformation, contained into string l, getting back the text t.
    :param l: last column of matrix M alphabetically sorted
    :param f: first column of matrix M alphabetically sorted (and consequently alphabetically sorted itself)
    :return: tc decompressed text
    """

    n = len(l)
    i = n - 1
    r = 0

    t = dict()

    sigma = set(list(l))
    c = dict()
    for s in sigma:
        c[s] = set_first_occurence(s, f)

    while i > 0:                    # symbol t[0] is '#'
        t[i] = l[r]
        i = i - 1
        r = c[l[r]] + rank(l, r)

    t = ''.join([t[i] for i in t])
    return t


def main():
    t = 'LABELLABALLA'
    print "\n\nText to be transformed: ", t

    l, f = bwt_direct(t)

    print "\n First column of matrix M alphabetically sorted: ", f
    print "\n BWT of text t: ", l

    t2 = bwt_inverse(l, f)
    print "\n Original text (correctness checking): ", t2


if __name__ == "__main__":
    main()
