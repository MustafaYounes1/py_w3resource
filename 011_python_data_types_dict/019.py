"""

Write a Python program to combine two dictionary by adding values for common keys.

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

{'a': 400, 'b': 400, 'd': 400, 'c': 300}

"""

from collections import Counter
from functools import reduce
from operator import add


def main():
    data = [
        {'a': 100, 'b': 200, 'c': 300},
        {'a': 300, 'b': 200, 'd': 400}
    ]

    # Counter + Counter would give the union of both Counters accumulating the values of common keys
    print(dict(reduce(add, map(Counter, data))))


if __name__ == "__main__":
    main()
