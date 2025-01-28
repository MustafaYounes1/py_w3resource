"""

Write a Python program to interleave multiple lists of the same length. Use the itertools module.

list1 = [100, 200, 300, 400, 500, 600, 700]
list2 = [10, 20, 30, 40, 50, 60, 70]
list3 = [1, 2, 3, 4, 5, 6, 7]

[100, 10, 1, 200, 20, 2, 300, 30, 3, 400, 40, 4, 500, 50, 5, 600, 60, 6, 700, 70, 7]

"""

from itertools import chain


def main():
    list1 = [100, 200, 300, 400, 500, 600, 700]
    list2 = [10, 20, 30, 40, 50, 60, 70]
    list3 = [1, 2, 3, 4, 5, 6, 7]

    print(list(chain.from_iterable(zip(list1, list2, list3))))


if __name__ == "__main__":
    main()
