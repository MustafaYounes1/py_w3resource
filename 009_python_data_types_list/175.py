"""

Write a Python program to find the minimum and maximum value for each tuple position in a given list of tuples.

[(2, 3), (2, 4), (0, 6), (7, 1)]

Maximum value for each tuple position in the said list of tuples:
[7, 6]

Minimum value for each tuple position in the said list of tuples:
[0, 1]

"""


def main():
    lst = [(2, 3), (2, 4), (0, 6), (7, 1)]

    print(list(map(max, zip(*lst))))
    print(list(map(min, zip(*lst))))


if __name__ == "__main__":
    main()
