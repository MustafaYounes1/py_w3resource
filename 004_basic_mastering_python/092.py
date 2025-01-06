"""

Create a dictionary with keys as numbers and values as their squares.

keys = [1, 2, 3, 4]

{1: 1, 2: 4, 3: 9, 4: 16}

"""


def main():
    keys = [1, 2, 3, 4]
    print(dict(zip(keys, list(map(lambda x: x**2, keys)))))


if __name__ == "__main__":
    main()
