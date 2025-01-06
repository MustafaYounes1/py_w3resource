"""

Write a Python program to get the left difference between two given lists, after applying the provided function to each
list element of both.

[2.1, 1.2], [2.3, 3.4], floor                       =>  [1.2]
[{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], v['x']      =>  [{'x': 2}]

"""

from math import floor
from operator import itemgetter


def main():
    lst1, lst2 = [2.1, 1.2], [2.3, 3.4]
    print([_ for _ in lst1 if floor(_) not in set(map(floor, lst2))])

    lst1, lst2 = [{'x': 2}, {'x': 1}], [{'x': 1}]
    print([_ for _ in lst1 if itemgetter('x')(_) not in set(map(itemgetter('x'), lst2))])


if __name__ == "__main__":
    main()
