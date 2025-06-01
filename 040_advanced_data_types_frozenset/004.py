"""

Write a Python program that implements a function to generate the power set (set of all subsets) of a given frozenset.

[1, 2, 3, 4]
   =>   frozenset()
        frozenset({1})
        frozenset({2})
        frozenset({1, 2})
        frozenset({3})
        frozenset({1, 3})
        frozenset({2, 3})
        frozenset({1, 2, 3})
        frozenset({4})
        frozenset({1, 4})
        frozenset({2, 4})
        frozenset({1, 2, 4})
        frozenset({3, 4})
        frozenset({1, 3, 4})
        frozenset({2, 3, 4})
        frozenset({1, 2, 3, 4})

"""

from itertools import combinations


def main():
    s = frozenset([1, 2, 3, 4])

    for r in range(0, len(s) + 1):
        for _ in combinations(s, r):
            i += 1
            print(frozenset(_))


if __name__ == "__main__":
    main()
