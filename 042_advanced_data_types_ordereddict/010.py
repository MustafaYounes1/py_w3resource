"""

Write a Python function that takes a list of words and returns an OrderedDict where keys are the words and values are
the lengths of the words.

["Red", "Green", "Pink", "White", "Orange"]
OrderedDict([('Red', 3), ('Green', 5), ('Pink', 4), ('White', 5), ('Orange', 6)])

"""

from collections import OrderedDict


def main():
    words = ["Red", "Green", "Pink", "White", "Orange"]
    d = OrderedDict({w: len(w) for w in words})
    print(d)


if __name__ == "__main__":
    main()
