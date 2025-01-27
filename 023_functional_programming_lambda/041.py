"""

Write a Python program to reverse strings in a given list of string values using lambda.

['Red', 'Green', 'Blue', 'White', 'Black']
['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

"""


def main():
    lst = ['Red', 'Green', 'Blue', 'White', 'Black']
    print(list(map(lambda _: _[::-1], lst)))


if __name__ == "__main__":
    main()
