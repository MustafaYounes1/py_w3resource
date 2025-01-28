"""

Write a Python program that generates the running product of elements in an iterable.

[1, 2, 3, 4, 5, 6, 7]   =>  [1, 2, 6, 24, 120, 720, 5040]

"""

from itertools import accumulate
from operator import mul


def main():
    lst = [1, 2, 3, 4, 5, 6, 7]
    print(list(accumulate(lst, mul)))


if __name__ == "__main__":
    main()
