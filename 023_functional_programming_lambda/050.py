"""

Write a Python program to find the maximum and minimum values in a given list of tuples using the lambda function.

[('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
(74, 62)

"""

from operator import itemgetter


def main():
    lst = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
    print(max(lst, key=itemgetter(1))[1], min(lst, key=itemgetter(1))[1])


if __name__ == "__main__":
    main()
