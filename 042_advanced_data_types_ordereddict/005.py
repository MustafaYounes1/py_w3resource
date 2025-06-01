"""

Write a Python program to create an OrderedDict with the following key-value pairs:

'Laptop': 40
'Desktop': 45
'Mobile': 35
'Charger': 25
Now move the 'Desktop' key to the end of the dictionary and print the updated contents.

OrderedDict([('Laptop', 40), ('Desktop', 45), ('Mobile', 35), ('Charger', 25)])
OrderedDict([('Laptop', 40), ('Mobile', 35), ('Charger', 25), ('Desktop', 45)])

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
    d.move_to_end('Desktop')
    print(d)


if __name__ == "__main__":
    main()
