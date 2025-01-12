"""

Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.

[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}

"""

from collections import defaultdict


def main():
    lst = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d = defaultdict(list)

    for k, v in lst:
        d[k].append(v)

    print(dict(d))


if __name__ == "__main__":
    main()
