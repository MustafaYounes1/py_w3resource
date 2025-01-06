"""

Write a Python program to round each float in a given list of numbers up to the next integer and return the running
total of the integer squares.

Input: [2.6, 3.5, 6.7, 2.3, 5.6]
Output:
[9, 25, 74, 83, 119]

Input: [301.1, 401.4, -23.1, 13554122.0, 10201.0101, 10000000.0]
Output:
[91204, 252808, 253337, 183714223444221, 183714327525025, 283714327525025]

"""

from itertools import accumulate
from math import ceil
from operator import add


def main():
    seq = list(map(lambda x: ceil(float(x)), input("Enter a list of comma-separated numbers: ").split(",")))
    print(list(accumulate([pow(_, 2) for _ in seq], add)))


if __name__ == "__main__":
    main()
