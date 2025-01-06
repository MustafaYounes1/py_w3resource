"""

Write a Python program to sort a given matrix in ascending order according to the sum of its rows.

[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
[[1, 1, 1], [1, 2, 3], [2, 4, 5]]

[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]

"""


def main():
    data = [
        [[1, 2, 3], [2, 4, 5], [1, 1, 1]],
        [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
    ]

    for _ in data:
        print(sorted(_, key=lambda _: sum(_)))


if __name__ == "__main__":
    main()
