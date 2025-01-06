"""

Calculate the Fibonacci sequence up to a given number of terms.

10      =>      [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

"""


def fib(n):
    if n == 0:
        return 0

    elif n in (1, 2):
        return 1

    else:
        return fib(n - 1) + fib(n - 2)


def main():
    n = 10
    print([fib(_) for _ in range(n)])


if __name__ == "__main__":
    main()
