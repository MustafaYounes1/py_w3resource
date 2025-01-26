"""

Write a Python function to calculate the factorial of a number (a non-negative integer).
The function accepts the number as an argument.

4   =>  24

"""


def factorial(n: int) -> int:
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    print(factorial(4))


if __name__ == "__main__":
    main()
