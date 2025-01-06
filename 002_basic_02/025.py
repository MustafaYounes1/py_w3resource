"""

Write a Python program to find the digits that are missing from a given mobile number.

    9832209763 -> 1, 4, 5

"""

from string import digits


def main():
    n = input("Enter the mobile number: ")
    print(set(digits) - set(n))


if __name__ == "__main__":
    main()
