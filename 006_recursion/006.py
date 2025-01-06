"""

Write a Python program to get the sum of a non-negative integer using recursion.
Test Data:
sumDigits(345) -> 12
sumDigits(45) -> 9

"""


def sum_digits(n):
    if not n:
        return 0

    else:
        return int(n[0]) + sum_digits(n[1:])


def main():
    n = input("Enter a number: ")
    print(sum_digits(n))


if __name__ == "__main__":
    main()
