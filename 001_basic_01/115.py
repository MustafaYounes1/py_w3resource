"""

 Write a Python program to compute the product of a list of integers (without using a for loop).

"""

from functools import reduce
import math


def main():
    seq = [int(_) for _ in input("Enter a list of space-separated integers: ").split()]

    # Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the
    # iterable to a single value.
    p = reduce(lambda x, y: x * y, seq)
    print(p)

    print("=" * 25)

    # Calculate the product of all the elements in the input iterable.
    print(math.prod(seq))


if __name__ == "__main__":
    main()
