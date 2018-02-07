# Program MAXIMUM in Python
# Figure 3.2 from the book "Il Pensiero Computazionale: dagli algoritmi al coding"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Il Mulino


def maximum(set):
    """
    Search of the maximum in a set of integers
    :param set: set of integers on which to seek the maximum
    """

    n = len(set)  # n is the number of elements of set

    max_val = set[0]

    # fa variare i da 1 a n-1
    for i in range(1, n):
        if set[i] > max_val:
            max_val = set[i]

    print "the maximum is %d" % max_val


def main():

    set = [24, 15, 7, 9, 20, 49, 33, 35, 22, 40, 52, 12, 62, 30, 8, 43]

    maximum(set)


if __name__ == "__main__":
    main()
