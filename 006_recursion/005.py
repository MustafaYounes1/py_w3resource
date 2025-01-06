"""

Write a Python program to solve the Fibonacci sequence with an input integer using recursion.

7   =>  13

"""


def fib(n):
    if not n:
        return 0

    elif n == 1:
        return 1

    else:
        return fib(n - 1) + fib(n - 2)


def main():
    n = 7
    print(fib(n))


if __name__ == "__main__":
    main()
