"""

Write a Python program to interleave multiple lists of the same length.

list1: [1, 2, 3, 4, 5, 6, 7]
list2: [10, 20, 30, 40, 50, 60, 70]
list3: [100, 200, 300, 400, 500, 600, 700]

[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]

"""


def main():
    data = [
        [1, 2, 3, 4, 5, 6, 7],
        [10, 20, 30, 40, 50, 60, 70],
        [100, 200, 300, 400, 500, 600, 700]
    ]

    print([_ for p in zip(*data) for _ in p])


if __name__ == "__main__":
    main()
