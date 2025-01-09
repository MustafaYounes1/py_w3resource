"""

Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
Note: average all nth numbers of the insider tuples (first_numbers, second_numbers, ...)

((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
[30.5, 34.25, 27.0, 23.25]

((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
[25.5, -18.0, 3.75]

"""

from statistics import mean


def main():
    data = [
        ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)),
        ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
    ]

    for _ in data:
        print(tuple(mean(__) for __ in zip(*_)))


if __name__ == "__main__":
    main()
