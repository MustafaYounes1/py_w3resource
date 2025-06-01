"""

Write a Python program that creates an OrderedDict and adds some items. Print the OrderedDict contents.

OrderedDict([('b', 98), ('c', 99), ('a', 97), ('f', 102), ('g', 103)])

"""

from collections import OrderedDict


def main():
    d: OrderedDict[str, int] = OrderedDict()

    for k in "bcafg":
        d[k] = ord(k)

    print(d)

if __name__ == "__main__":
    main()
