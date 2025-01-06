"""

Write a Python program to get the factorial of a non-negative integer using recursion.

5   =>  120

"""


def factorial(n):
    if n == 1:
        return 1

    else:
        return n * factorial(n - 1)


def main():
    n = 5
    print(factorial(n))


if __name__ == "__main__":
    main()
