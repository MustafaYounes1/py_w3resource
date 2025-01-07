"""

Write a Python program to find all the pairs in a list whose sum is equal to a given value.

[1, 2, 3, 4, 5, 6, 7, 8, 9], 10     =>  [(6, 4), (7, 3), (8, 2), (9, 1)]
[1, 2, 3, 4, 5, 6, 7, 8, 9], 35     =>  []
[1, 2, 3, 4, 5, 6, 7, 8, 9], 5      =>  [(3, 2), (4, 1)]

"""

from itertools import combinations


def main():
    data = [
        [[1, 2, 3, 4, 5, 6, 7, 8, 9], 10],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9], 35],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9], 5]
    ]

    for lst, s in data:
        print(
            list(
                filter(
                    lambda _: sum(_) == s,
                    combinations(lst, 2)
                )
            )
        )


if __name__ == "__main__":
    main()
