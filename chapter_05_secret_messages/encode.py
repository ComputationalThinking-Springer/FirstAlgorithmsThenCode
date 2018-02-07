# Program ENCODE in Python
# Figure 6.3 from the book "Il Pensiero Computazionale: dagli algoritmi al coding"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Il Mulino


# loads trasform
from transform import transform


def encode():
    """
    Transforms a message into the relative cryptogram by applying
    a translation module 26 of k positions in the alphabet, 
    where k is the cypher key.
    """

    k = int(raw_input('give me the key: '))

    msg = raw_input('give me the message: ')        # msg is a vector of 140 characters containing the message

    crt = [''] * 140                                # crt is a vector of 140 characters containing the cryptogram
    for h in range(0, 140):
        if h < len(msg):
            t = transform(k, msg[h])
            crt[h] = t

    print ''.join(crt)


def main():

    encode()


if __name__ == "__main__":
    main()


"""
Example of interaction with the user
python cifra.py
give me the key: 3
give me the message: PENSIEROCOMPUTAZIONALE
SHQVLHURFRPSXWDCLRQDOH 
Process finished with exit code 0
"""