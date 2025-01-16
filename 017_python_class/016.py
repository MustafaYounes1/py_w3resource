"""

Write a Python class to get all possible unique subsets from a set of distinct integers.

[4, 5, 6]
[(), (6,), (4,), (5,), (4, 5), (4, 6), (5, 6), (4, 5, 6)]

"""

from itertools import combinations


class Solver:
    @staticmethod
    def solve(lst: list) -> list:
        return [_ for idx in range(0, len(lst) + 1) for _ in set(combinations(lst, idx))]


def main():
    print(Solver.solve([4, 5, 6]))


if __name__ == "__main__":
    main()
