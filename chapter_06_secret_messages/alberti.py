# Program ALBERTI in Python
# Figure 6.6 from the book "Il Pensiero Computazionale: dagli algoritmi al coding"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Il Mulino


def alberti():
    """
    Transforms a message into the relative cryptogram by applying the method of Leon Battista Alberti, 
    where k is the cypher key.
    """

    outer = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', '1', '2', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', '3', '4', '5', 'Z']

    inner = ['F', 'B', 'M', 'K', 'R', 'O', 'A', 'V', 'T', 'Z', 'Y', 'C', 'G',
             'N', 'L', 'X', 'P', 'Q', 'H', 'J', 'D', 'I', 'E', 'U', 'S', 'W']

    k = 0   # k (the key) is the entity of the counterclockwise roation of the inner disc with respect to the outer disc

    msg = raw_input('give me the message: ')       # msg is a vector of 140 characters containing the message

    crt = [' '] * 140                              # crt is a vector of 140 characters containing the cryptogram

    for h in range(0, 140):
        if h < len(msg):
            i = 0
            while msg[h] != outer[i]:              # search msg[h] in outer
                i = i + 1
            j = (i + k) % 26                       # now msg[h] = outer[i]
            crt[h] = inner[j]
            if outer[i] in ['1', '2', '3', '4', '5']:
                k = (i + k) % 26                   # msg[h] is a special character: the operation update the key

    print ''.join(crt)


def main():

    alberti()


if __name__ == "__main__":
    main()


"""
Example of interaction with the user
python alberti.py
give me the message: BUONA3SERA
BDLNFELFNE                                                                                                                                  
Process finished with exit code 0
"""