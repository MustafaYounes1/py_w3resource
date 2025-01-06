"""

Write a Python program to compute the product of the odd digits in a given number, or 0 if there aren't any.

Input: 123456789
Output:
945

Input: 2468
Output:
0

Input: 13579
Output:
945

"""

from math import prod


def main():
    n = input("Enter a number: ")
    odds = [int(d) for d in n if (int(d) % 2) != 0]
    res = prod(odds) if odds else 0
    print(res)


if __name__ == "__main__":
    main()
