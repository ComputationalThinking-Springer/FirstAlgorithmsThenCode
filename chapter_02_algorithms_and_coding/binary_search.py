# Program BINARY_SEARCH in Python
# Figure 2.8 from the book "Computational Thinking: First Algorithms, Then Code"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Springer


# loads mathematical functions
import math


def binary_search(set, data):
    """
    Binary search of a given element in a sorted set
    :param set: set to search in
    :param data: data to search for
    """

    n = len(set)  # n is the number of elements of set

    i = 0
    j = n - 1

    while i <= j:
        # math.floor() gets the closest integer <= x
        # int() removes the comma
        # m is the central position between i and j

        m = int(math.floor((i + j) / 2))

        if data == set[m]:
            print "%s is present" % data
            return
        if data < set[m]:
            j = m - 1
        if set[m] < data:
            i = m + 1

    print "%s is not present" % data


def main():

    city = ['FI', 'MI', 'PA', 'NA', 'BO', 'TO', 'VE', 'CA']

    binary_search(city, 'NA')

    binary_search(city, 'RC')


if __name__ == "__main__":
    main()
