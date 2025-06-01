"""

Write a Python program that reverses the order of a given OrderedDict.

OrderedDict([('c', 99), ('b', 98), ('a', 97)])
OrderedDict([('a', 97), ('b', 98), ('c', 99)])

"""

from collections import OrderedDict


def main():
    d = OrderedDict()

    for _ in "cba":
        d[_] = ord(_)

    print(d)

    d = OrderedDict({k: d.get(k) for k in reversed(d)})
    print(d)


if __name__ == "__main__":
    main()
