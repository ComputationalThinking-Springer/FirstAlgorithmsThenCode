# Program PERMUTATIONS in Python
# Figure 10.8 from the book "Il Pensiero Computazionale: dagli algoritmi al coding"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Il Mulino


def explore(p):
    print p


def permutations(p, k):
    """
    Permutations of the elements of a subvector p[k:n-1], inclusive
    :param p: vector to permute
    :param k: lower index of the vector p
    """

    n = len(p)

    if k == n - 1:
        explore(p)
    else:
        for i in range(k, n):
            p[i], p[k] = p[k], p[i]     # scambia p[k] con p[i]
            permutations(p, k + 1)
            p[i], p[k] = p[k], p[i]     # ripristina la situazione originaria


def main():

    city = ['FI', 'MI', 'PA']

    permutations(city, 0)


if __name__ == "__main__":
    main()
