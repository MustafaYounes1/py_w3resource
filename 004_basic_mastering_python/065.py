"""

Convert a dictionary to a list of tuples.

d = {'a': 1, 'b': 2, 'c': 3}    =>      [('a', 1), ('b', 2), ('c', 3)]

"""


def main():
    d = {'a': 1, 'b': 2, 'c': 3}
    print(list(d.items()))


if __name__ == "__main__":
    main()
