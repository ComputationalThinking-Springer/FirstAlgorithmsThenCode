# Program LOAD_SEARCH in Python
# Figure 2.6 from the book "Il Pensiero Computazionale: dagli algoritmi al coding"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Il Mulino


# loads the program search2
from search2 import search2


def load_search():
    """
    Program to query the computer about the information associated 
    with a list name through the search call2.
    :return: 
    """
    city = ['FI', 'MI', 'PA', 'NA', 'BO', 'TO', 'VE', 'CA']
    prefix = ['055', '02', '091', '081', '051', '011', '041', '070']

    # search is a control parameter.
    # For search == 'GO' the search continues
    # For search == 'ALT' the search stops
    search = 'GO'

    while search == 'GO':
        name = raw_input('data to search for: ')
        search2(city, prefix, name)
        search = raw_input('continue? ')


def main():

    load_search()


if __name__ == "__main__":
    main()


"""
Example of interaction with the user
python load_search.py
data to search for: NA
the information corresponding to NA is 081
continue? GO
data to search for: RG
RG data to search for: 
continue? ALT
Process finished with exit code 0
"""