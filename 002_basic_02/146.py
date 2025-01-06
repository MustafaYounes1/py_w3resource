"""

A Python list contains two positive integers. Write a Python program to check whether the cube root of the first
number is equal to the square root of the second number.

Sample Data:
([8, 4]) ->     True
([64, 16]) ->   True
([64, 36]) ->   False

"""

from math import sqrt, cbrt


def main():
    seq = list(map(int, input("Enter a list of comma-separated numbers: ").split(", ")))
    print(cbrt(seq[0]) == sqrt(seq[1]))


if __name__ == "__main__":
    main()
