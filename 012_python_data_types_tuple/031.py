"""

Write a Python program to compute the element-wise sum of given tuples.

(1, 2, 3, 4)
(3, 5, 2, 1)
(2, 2, 3, 1)

(6, 9, 8, 6)

"""


def main():
    lst = [
        (1, 2, 3, 4),
        (3, 5, 2, 1),
        (2, 2, 3, 1)
    ]

    print(tuple(map(sum, zip(*lst))))


if __name__ == "__main__":
    main()
