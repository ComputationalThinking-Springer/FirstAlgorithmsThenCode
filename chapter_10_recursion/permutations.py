# Program PERMUTATIONS in Python
# Figure 10.8 from the book "Computational Thinking: First Algorithms, Then Code"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Springer


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
            p[i], p[k] = p[k], p[i]     # swap p[k] with p[i]
            permutations(p, k + 1)
            p[i], p[k] = p[k], p[i]     # reset the original vector content


def main():

    city = ['FI', 'MI', 'PA']

    permutations(city, 0)


if __name__ == "__main__":
    main()
