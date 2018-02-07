# Program REC_TH in Python
# Figure 10.3 from the book "Il Pensiero Computazionale: dagli algoritmi al coding"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Il Mulino


def rec_th(i, x, y, z):
    """
    A recursive solution for the Hanoi Tower problem. 
    The discs are n and the pegs are a,b,c, but the program refers to a generic phase in which 
    are moved the discs in which are moved the smallest discs from a peg x to a peg y by using a temporary peg z.
    :param i: number of discs
    :param x: peg x
    :param y: peg y
    :param z: peg z
    """

    if i == 1:
        y.append(x.pop())   # extreme situation with a unique disc
        return

    rec_th(i - 1, x, z, y)
    y.append(x.pop())
    rec_th(i - 1, z, y, x)


def main():

    a = [4, 3, 2, 1]
    b = []
    c = []

    print a
    print b
    print c

    print ''

    rec_th(4, a, b, c)

    print a
    print b
    print c


if __name__ == "__main__":
    main()
