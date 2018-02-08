# Program SEARCH2 in Python
# Figure 2.4 from the book "Computational Thinking: First Algorithms, Then Code"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Springer


def search2(set, info, data):
    """
    Search the information associated with a given element.
    :param set: set to search in
    :param info: vector of information
    :param data: data to search for
    """

    n = len(set)       # n is the number of elements of set

    i = 0
    while i <= n - 1:
        if set[i] == data:
            print "the information corresponding to %s is %s" % (data, info[i])
            return
        else:
            i = i + 1

    print "%s is not present" % data


def main():

    city = ['FI', 'MI', 'PA', 'NA', 'BO', 'TO', 'VE', 'CA']
    prefix = ['055', '02', '091', '081', '051', '011', '041', '070']

    search2(city, prefix, 'NA')

    search2(city, prefix, 'RC')


if __name__ == "__main__":
    main()
