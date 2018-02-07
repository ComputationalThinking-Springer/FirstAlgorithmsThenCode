# Program REC_BS in Python
# Figure 10.6 from the book "Il Pensiero Computazionale: dagli algoritmi al coding"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Il Mulino


# loads mathematical functions
import math


def rec_bs(set, i, j, data):
    """
    Recursive version of binary search of an element in a given set.
    :param set: orderd set on which to search on
    :param i: lower index of vector set
    :param j: upper index of vector set
    :param data: data to search for
    """

    if i > j:
        print "\n %s is not present" % data
        return

    m = int(math.floor((i + j) / 2))

    if data == set[m]:
        print "\n %s is present" % data
        return
    elif data < set[m]:
        rec_bs(set, i, m - 1, data)
    else:
        rec_bs(set, m + 1, j, data)


def main():

    city = ['FI', 'MI', 'PA', 'NA', 'BO', 'TO', 'VE', 'CA']

    print "\n Vector to search on: ", city

    rec_bs(city, 0, len(city) - 1, 'NA')

    rec_bs(city, 0, len(city) - 1, 'RC')


if __name__ == "__main__":
    main()
