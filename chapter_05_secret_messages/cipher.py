# Program ENCODE in Python
# Figure 5.2 from the book "Computational Thinking: First Algorithms, Then Code"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Springer


# loads trasform
from transform import transform


def cipher():
    """
    Transforms a message into the relative cryptogram by applying
    a sum module 26 of k positions in the alphabet, 
    where k is the cypher key.
    """

    k = int(raw_input('communicate the key: '))

    msg = raw_input('communicate the message: ')       # msg is a vector of 140 characters containing the message

    crt = [''] * 140                                # crt is a vector of 140 characters containing the cryptogram
    for h in range(0, 140):
        if h < len(msg):
            t = transform(k, msg[h])
            crt[h] = t

    print ''.join(crt)


def main():

    cipher()


if __name__ == "__main__":
    main()


"""
Example of interaction with the user
python cipher.py
communicate the key: 3
communicate the message: PENSIEROCOMPUTAZIONALE
SHQVLHURFRPSXWDCLRQDOH 
Process finished with exit code 0
"""
