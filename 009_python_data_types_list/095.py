"""

Write a Python program to sort each sublist of strings in a given list of lists.

[["green", "orange"], ["black", "white"], ["white", "black", "orange"]]
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

"""

from operator import itemgetter


def main():
    lst = [["green", "orange"], ["black", "white"], ["white", "black", "orange"]]
    print([sorted(_, key=itemgetter(0, 1)) for _ in lst])


if __name__ == "__main__":
    main()
