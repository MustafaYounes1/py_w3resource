"""

Merge two dictionaries.

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

{'a': 1, 'b': 3, 'c': 4}

"""


def main():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    out = {**dict1, **dict2}
    print(out)


if __name__ == "__main__":
    main()
