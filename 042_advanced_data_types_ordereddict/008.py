"""

Write a Python function that creates an OrderedDict and removes a key-value pair from the OrderedDict using a given key.

'Laptop': 40
'Desktop': 45
'Mobile': 35
'Charger': 25

Key to remove: 'Desktop'

OrderedDict([('Laptop', 40), ('Mobile', 35), ('Charger', 25)])

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

    d.pop("Desktop")
    print(d)


if __name__ == "__main__":
    main()
