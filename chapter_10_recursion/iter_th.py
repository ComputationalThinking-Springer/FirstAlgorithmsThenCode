# Program ITER_TH in Python
# Figure 10.5 from the book "Computational Thinking: First Algorithms, Then Code"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Springer


def iter_th(n, p):
    """
    Iterative algorithm to solve for the Hanoi Tower problem.
    The order in which are considered the pegs is different for n odd or even.
    :param n: number of discs
    :param p: vector of pegs
    """

    k = 0

    index = 1 if n % 2 == 1 else 2  # if n is even, A,B,C, otherwise A,C,B

    iter_index = 0
    while len(p[index]) < n:

        print iter_index, p[0], p[1], p[2]

        # move disc 1
        p[(k + 1) % 3].append(p[k].pop())

        # move the only possible disc between the other pegs
        if (len(p[k]) > 0) and (len(p[(k + 2) % 3]) > 0):
            if p[k][-1] < p[(k + 2) % 3][-1]:
                p[(k + 2) % 3].append(p[k].pop())
            else:
                p[k].append(p[(k + 2) % 3].pop())
        elif (len(p[k]) > 0) and (len(p[(k + 2) % 3]) == 0):
            p[(k + 2) % 3].append(p[k].pop())
        elif (len(p[k]) == 0) and (len(p[(k + 2) % 3]) > 0):
            p[k].append(p[(k + 2) % 3].pop())

        k = (k + 1) % 3
        iter_index = iter_index + 1


def main():
    a = [5, 4, 3, 2, 1]
    b = []
    c = []

    p = [a, b, c]

    iter_th(len(a), p)

    print ''
    print a
    print b
    print c


if __name__ == "__main__":
    main()
