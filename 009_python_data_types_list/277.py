"""

Write a Python program to calculate the largest and smallest gap between sorted elements of a list of integers.

[1, 2 ,9, 0, 4, 6]          -> (3, 1)
[23, -2, 45, 38, 12, 4, 6]  -> (15, 2)

"""


def main():
    data = [
        [1, 2, 9, 0, 4, 6],
        [23, -2, 45, 38, 12, 4, 6]
    ]

    for lst in data:
        lst.sort()
        res = [b - a for a, b in zip(lst[:-1], lst[1:])]
        print((max(res), min(res)))


if __name__ == "__main__":
    main()
