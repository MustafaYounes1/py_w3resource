"""

Replace all values in a list with the mean of the list.

lst = [10, 20, 30, 40, 50]      =>      [30.0, 30.0, 30.0, 30.0, 30.0]
"""

from statistics import mean


def main():
    lst = [10, 20, 30, 40, 50]
    print([mean(lst)] * len(lst))


if __name__ == "__main__":
    main()
