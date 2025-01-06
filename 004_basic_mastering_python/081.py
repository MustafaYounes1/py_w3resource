"""

Sort a list of tuples by the second element.

[(1, 3), (2, 2), (3, 1)]    =>      [(3, 1), (2, 2), (1, 3)]

"""


def main():
    lst = [(1, 3), (2, 2), (3, 1)]
    print(sorted(lst, key=lambda x: x[1]))


if __name__ == "__main__":
    main()
