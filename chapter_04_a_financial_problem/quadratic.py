# Program QUADRATIC in Python
# Figure 4.3 from the book "Computational Thinking: First Algorithms, Then Code"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Springer


def quadratic(d):
    """
    Calculates the portion d[a: v] with the maximum sum
    by testing all the possible intervals [i,j] in [1,n-1] inclusive
    :param d: vector of positive and negative numbers, d[0] initial value of the action
    """

    n = len(d)  # n is the number of elements of d

    max_sum = -float('inf')
    a = 1
    v = 0

    for i in range(1, n):
        tmp = 0                      # tmp is a temporary value
        for j in range(i, n):
            tmp = tmp + d[j]
            if tmp > max_sum:
                max_sum = tmp
                a = i
                v = j

    print "The maximum gain is %d" % max_sum
    print "It is realized within the range of days [%d,%d]" % (a, v)
    print "Portion of d with maximum sum %s" % d[a:v + 1]


def main():

    d = [10, +4, -6, +3, +1, +3, -2, +3, -4, +1, -9, +6]

    quadratic(d)


if __name__ == "__main__":
    main()
