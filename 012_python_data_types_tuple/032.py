"""

Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.

[(1, 2), (2, 3), (3, 4)]
[3, 5, 7]

[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
[9, -1, 7, 8]

"""


def main():
    data = [
        [(1, 2), (2, 3), (3, 4)],
        [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
    ]

    for _ in data:
        print(list(map(sum, _)))


if __name__ == "__main__":
    main()
