# Program FIB in Python
# Figure 10.14 from the book "Il Pensiero Computazionale: dagli algoritmi al coding"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Il Mulino


def fib(n):
    """
    Iterative calculus and print the n-th Fibonacci number.
    :param n: Fibonacci number
    """

    a = 1
    b = 1                   # set a = F_1 and b = F_2

    for i in range(3, n+1):
        c = a + b
        a = b
        b = c               # set a = F_{i-1} and b = F_{i}

    print "F_%d = %d" % (n, b)


def main():

    fib(12)


if __name__ == "__main__":
    main()
