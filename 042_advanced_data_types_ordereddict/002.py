"""

Write a Python program that sorts the OrderedDict by its keys. Sort the OrderedDict by its values as well.

'Laptop': 40
'Desktop': 45
'Mobile': 35

-> sorted according to the keys:    OrderedDict([('Desktop', 45), ('Laptop', 40), ('Mobile', 35)])
-> sorted according to the values:  OrderedDict([('Mobile', 35), ('Laptop', 40), ('Desktop', 45)])
"""

from collections import OrderedDict
from operator import itemgetter


def main():
    d = OrderedDict(
        {
            'Laptop': 40,
            'Desktop': 45,
            'Mobile': 35
        }
    )

    print(OrderedDict(sorted(d.items(), key=itemgetter(0))))
    print(OrderedDict(sorted(d.items(), key=itemgetter(1))))


if __name__ == "__main__":
    main()
