"""

Write a Python program to insert an element at the beginning of a given Ordered Dictionary.

[('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')]

Insert an element at the beginning of the said OrderedDict: ('color4', 'Orange')

[('color4', 'Orange'), ('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')]

"""

from collections import OrderedDict


def main():
    d = OrderedDict([('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')])

    d['color4'] = 'Orange'
    d.move_to_end('color4', last=False)

    print(list(d.items()))

if __name__ == "__main__":
    main()
