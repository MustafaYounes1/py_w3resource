"""

Create a dictionary with a default value.

keys = ['a', 'b', 'c']
value = 1

{'a': 1, 'b': 1, 'c': 1}

"""


def main():
    keys = ['a', 'b', 'c']
    print(dict.fromkeys(keys, 1))


if __name__ == "__main__":
    main()
