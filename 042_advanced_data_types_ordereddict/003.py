"""

Write a Python program that accesses an item in the OrderedDict by its key. Check if a specified item exists in the
OrderedDict as well.

"""

from collections import OrderedDict


def main():
    d = OrderedDict({v: v for v in range(10)})
    print(0 in d)
    print(d[0])


if __name__ == "__main__":
    main()
