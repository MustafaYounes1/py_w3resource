"""

Write a Python program to find the common tuples between two given lists.

[('red', 'green'), ('black', 'white'), ('orange', 'pink')]
[('red', 'green'), ('orange', 'pink')]

[('orange', 'pink'), ('red', 'green')]

"""


def main():
    lst1 = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
    lst2 = [('red', 'green'), ('orange', 'pink')]

    print(set(lst1) & set(lst2))


if __name__ == "__main__":
    main()
