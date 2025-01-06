"""

Write a Python program to sort a given list of tuples by a specified element.

[('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]

1st element =>  [('item1', 11, 24.5), ('item2', 10, 10.12), ('item3', 15, 25.1), ('item4', 12, 22.5)]
2nd element =>  [('item2', 10, 10.12), ('item1', 11, 24.5), ('item4', 12, 22.5), ('item3', 15, 25.1)]
3rd element =>  [('item2', 10, 10.12), ('item4', 12, 22.5), ('item1', 11, 24.5), ('item3', 15, 25.1)]

"""

from operator import itemgetter


def main():
    lst = [('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]

    for idx in (0, 1, 2):
        print(sorted(lst, key=itemgetter(idx)))


if __name__ == "__main__":
    main()
