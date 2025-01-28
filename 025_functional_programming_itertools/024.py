"""

Write a Python program to find the pairs of elements from a given list whose sum is equal to a given value.
Use the itertools module to solve the problem.

[1, 2, 3, 4, 5, 6, 7], 10       =>  [(3, 7), (4, 6)]
[1, 2, -3, -4, -5, 6, -7], -6   =>  [(1, -7)]

"""

from itertools import combinations


def main():
    data = [
        ([1, 2, 3, 4, 5, 6, 7], 10),
        ([1, 2, -3, -4, -5, 6, -7], -6)
    ]

    for lst, n in data:
        print(list(filter(lambda _: sum(_) == n, combinations(lst, 2))))


if __name__ == "__main__":
    main()
