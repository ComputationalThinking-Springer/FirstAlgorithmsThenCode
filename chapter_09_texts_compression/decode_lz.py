# Program DECODE_LZ in Python
# Figure 9.6 from the book "Il Pensiero Computazionale: dagli algoritmi al coding"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Il Mulino


# loads encode_lz
from encode_lz import *


def decode_lz(c):
    """
    Algorithm of Lempel e Ziv for the inverse transformation from a sequence of couples c to the original text t.
    :param t: c couples (0 or previous distance of appearance, single letter or repeated substring length) 
    :return: decompressed text
    """

    i = 0
    t = dict()

    while len(c) > 0:
        a, b = c.pop(0)         # extracts the first couple, let be (a, b)
        if a == 0:
            t[i] = b
            i = i + 1
        else:                   # copy a substring with length 'b' at distance 'a'
            for k in range(0, b):
                t[i + k] = t[i - a + k]
            i = i + b

    t = ''.join([t[i] for i in t])
    return t


def main():
    t = 'LABELLABALLA'
    print "\n input text: ", t

    c = encode_lz(t)
    print "\n sequence of couples: ", c

    t2 = decode_lz(c)
    print "\n text for sequence of couples (for correctness control): ", t2


if __name__ == "__main__":
    main()
