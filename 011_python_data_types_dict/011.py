"""

Write a Python program to multiply all the items in a dictionary.

my_dict = {'data1': 100, 'data2': -54, 'data3': 247}

    =>  -1333800

"""

from math import prod


def main():
    my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
    print(prod(my_dict.values()))


if __name__ == "__main__":
    main()
