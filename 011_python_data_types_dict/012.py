"""

Write a Python program to remove a key from a dictionary.

myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

remove 'c'

"""


def main():
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    del my_dict['c']
    print(my_dict)


if __name__ == "__main__":
    main()
