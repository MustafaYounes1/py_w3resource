"""

Write a Python program to remove empty lists from a given list of lists.

[[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]

['Red', 'Green', [1, 2], 'Blue']

"""


def main():
    lst = [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
    print(list(filter(lambda _: not (isinstance(_, list) and not _), lst)))


if __name__ == "__main__":
    main()
