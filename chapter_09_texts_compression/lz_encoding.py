# Program LZ_ENCODING in Python
# Figure 9.5 from the book "Computational Thinking: First Algorithms, Then Code"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Springer


def find_the_longest_substring(t, i):
    n = len(t)
    j = i - 1
    max_l = 0
    max_dist = 0
    while j >= 0:
        for l in range(1, n-i+1):
            if t[i: i + l] == t[j: j + l]:
                if l > max_l:
                    max_l = l
                    max_dist = i-j

        j = j - 1
    return max_l, max_dist


def lz_encoding(t):
    """
    Lempel-Ziv algorithm to trasform the text t into a sequence of pairs c.
    :param t: text to compress
    :return: pairs having the form (0 or distance of previous occurrence of substring, single letter or repeated substring length) 
    """

    n = len(t)
    i = 0
    c = list()

    while i < n:
        l, dist = find_the_longest_substring(t, i)    # find the longest repeated substring starting at i
        if l == 0:                                    # t[i] appears for the first time
            c.append((0, t[i]))
            i = i + 1
        else:                                         # that is, it does exist a copy with length l > 0
            c.append((dist, l))
            i = i + l

    return c


def main():

    t = 'LABELLABALLA'
    print "\n Input text: ", t

    c = lz_encoding(t)
    print "\n Sequence of pairs: ", c


if __name__ == "__main__":
    main()
