"""

Write a Python program to convert a given list of strings into a list of lists using the map function.

["Red", "Green", "Black", "Orange"]
[['R', 'e', 'd'], ['G', 'r', 'e', 'e', 'n'], ['B', 'l', 'a', 'c', 'k'], ['O', 'r', 'a', 'n', 'g', 'e']]

"""


def main():
    lst = ["Red", "Green", "Black", "Orange"]
    print(list(map(list, lst)))


if __name__ == "__main__":
    main()
