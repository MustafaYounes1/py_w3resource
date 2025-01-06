"""

Write a Python program to remove all values except integer values from a given array of mixed values.

[34.67, 12, -94.89, 'Python', 0, 'C#']
[12, 0]

"""


def main():
    lst = [34.67, 12, -94.89, 'Python', 0, 'C#']
    print(list(filter(lambda _: isinstance(_, int), lst)))


if __name__ == "__main__":
    main()
