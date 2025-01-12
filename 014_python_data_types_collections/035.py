"""

Write a Python program to group a sequence of key-value pairs into a dictionary of lists.

class_roll = [('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]

[('v', [1, 3]), ('vi', [2, 4]), ('vii', [1])]

"""

from collections import defaultdict


def main():
    class_roll = [('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]
    d = defaultdict(list)

    for k, v in class_roll:
        d[k].append(v)

    print(list(d.items()))


if __name__ == "__main__":
    main()
