# Program ENCODE_LZ in Python
# Figure 9.5 from the book "Il Pensiero Computazionale: dagli algoritmi al coding"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Il Mulino


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


def encode_lz(t):
    """
    Algorithm of Lempel e Ziv for trasforming the text t into a sequence of couples c.
    :param t: text to compress
    :return: couples with the form (0 or previous distance of appearance, single letter or repeated substring length) 
    """

    n = len(t)
    i = 0
    c = list()

    while i < n:
        l, dist = find_the_longest_substring(t, i)    # find the longest repeated substring appearing in i
        if l == 0:                                    # t[i] appears for teh first time
            c.append((0, t[i]))
            i = i + 1
        else:                                         # that is, exists a copy with length l > 0
            c.append((dist, l))
            i = i + l

    return c


def main():

    t = 'LABELLABALLA'
    print "\n Testo in input: ", t

    c = encode_lz(t)
    print "\n Sequenza di coppie: ", c


if __name__ == "__main__":
    main()
