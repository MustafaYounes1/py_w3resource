"""

Convert a list of tuples to a dictionary.

lst = [('a', 1), ('b', 2), ('c', 3)]    =>  {'a': 1, 'b': 2, 'c': 3}

"""


def main():
    lst = [('a', 1), ('b', 2), ('c', 3)]
    print(dict(lst))


if __name__ == "__main__":
    main()
