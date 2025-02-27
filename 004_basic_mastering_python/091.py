"""

Merge two lists into a dictionary, using one as keys and the other as values.

keys = ['a', 'b', 'c']
values = [1, 2, 3]

{'a': 1, 'b': 2, 'c': 3}

"""


def main():
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    print(dict(zip(keys, values)))


if __name__ == "__main__":
    main()
