"""

Write a Python program to create an OrderedDict with the following key-value pairs:

'Laptop': 40
'Desktop': 45
'Mobile': 35
'Charger': 25
Now remove the first key-value pair and print the updated OrderedDict.

OrderedDict([('Laptop', 40), ('Desktop', 45), ('Mobile', 35), ('Charger', 25)])
OrderedDict([('Desktop', 45), ('Mobile', 35), ('Charger', 25)])

"""

from collections import OrderedDict


def main():
    d = OrderedDict(
        {
            'Laptop': 40,
            'Desktop': 45,
            'Mobile': 35,
            'Charger': 25
        }
    )

    print(d)

    d.popitem(last=False)
    print(d)


if __name__ == "__main__":
    main()
