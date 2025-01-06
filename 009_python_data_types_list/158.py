"""

Write a Python program to find the maximum and minimum values in a given list of tuples.

[('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]

(78, 60)

"""

from operator import itemgetter


def main():
    lst = [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
    print(max(lst, key=itemgetter(1)), min(lst, key=itemgetter(1)))


if __name__ == "__main__":
    main()
