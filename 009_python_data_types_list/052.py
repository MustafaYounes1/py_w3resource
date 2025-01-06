"""

Write a Python program to compute the difference between two lists.

["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]

Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']

"""


def main():
    lst1, lst2 = ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
    print(set(lst1) - set(lst2))
    print(set(lst2) - set(lst1))


if __name__ == "__main__":
    main()
