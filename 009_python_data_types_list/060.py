"""

Write a Python program to find a tuple, the smallest second index value from a list of tuples.

x = [(4, 1), (1, 2), (6, 0)]

(6, 0)

"""

from operator import itemgetter


def main():
    x = [(4, 1), (1, 2), (6, 0)]
    print(min(x, key=itemgetter(1)))


if __name__ == "__main__":
    main()
