"""

Find the median of a list of numbers.

e.g.    lst = [2, 5, 1, 3, 4]       =>      3

"""

from statistics import median


def main():
    lst = [2, 5, 1, 3, 4]
    print(median(lst))


if __name__ == "__main__":
    main()
