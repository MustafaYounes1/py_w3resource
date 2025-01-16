"""

Write a Python class to find the three elements that sum to zero from a set of n real numbers.

[-25, -10, -7, -3, 2, 4, 8, 10]

[[-10, 2, 8], [-7, -3, 10]]

"""

from itertools import combinations


class Solver:
    @classmethod
    def solve(cls, lst: list) -> list:
        return list(filter(lambda _: sum(_) == 0, combinations(lst, 3)))


def main():
    print(Solver.solve([-25, -10, -7, -3, 2, 4, 8, 10]))


if __name__ == "__main__":
    main()
