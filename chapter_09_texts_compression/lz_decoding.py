# Program LZ_DECODING in Python
# Figure 9.6 from the book "Computational Thinking: First Algorithms, Then Code"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Springer


# loads encode_lz
from encode_lz import *


def decode_lz(c):
    """
    Lempel-Ziv algorithm for the inverse transformation from a sequence of pairs c to the original text t.
    :param t: c pairs (0 or distance of previous substring occurrence, single letter or repeated substring length) 
    :return: decompressed text
    """

    i = 0
    t = dict()

    while len(c) > 0:
        a, b = c.pop(0)         # extracts the first pair, let it be <a, b>
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
    print "\n sequence of pairs: ", c

    t2 = decode_lz(c)
    print "\n text derived from the pairs sequence (for correctness check): ", t2


if __name__ == "__main__":
    main()
