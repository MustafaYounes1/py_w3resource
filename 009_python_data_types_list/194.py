"""

Write a Python program to sum two or more lists. The lengths of the lists may be different.

[[1, 2, 4], [2, 4, 4], [1, 2]]  =>  [4, 8, 8]
[[1], [2, 4, 4], [1, 2], [4]]   =>  [8, 6, 4]

"""

from itertools import zip_longest


def main():
    data = [
        [[1, 2, 4], [2, 4, 4], [1, 2]],
        [[1], [2, 4, 4], [1, 2], [4]]
    ]

    for _ in data:
        print(list(map(sum, zip_longest(*_, fillvalue=0))))


if __name__ == "__main__":
    main()
