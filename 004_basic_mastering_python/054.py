"""

Flatten a list of lists.

e.g.    lst = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]     =>  [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""

from itertools import chain


def main():
    lst = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    print(list(chain.from_iterable(lst)))


if __name__ == "__main__":
    main()
