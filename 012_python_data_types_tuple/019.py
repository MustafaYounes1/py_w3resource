"""

Write a Python program to convert a list of tuples into a dictionary.
Note: the key is the first element and it's not unique  =>  group all of the keys into lists

[("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]

{'x': [1, 2, 3], 'y': [1, 2], 'z': [1]}

"""

from collections import defaultdict


def main():
    lst = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
    out = defaultdict(list)

    for p in lst:
        out[p[0]].append(p[1])

    print(dict(out))


if __name__ == "__main__":
    main()
