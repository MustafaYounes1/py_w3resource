"""

Write a Python program to convert a given list of tuples to a list of strings using the map function.

[('red', 'pink'), ('white', 'black'), ('orange', 'green')]
['red pink', 'white black', 'orange green']

"""


def main():
    lst = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
    print(list(map(" ".join, lst)))


if __name__ == "__main__":
    main()
