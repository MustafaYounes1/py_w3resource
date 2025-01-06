"""

Write a Python program to reverse strings in a given list of string values.

['Red', 'Green', 'Blue', 'White', 'Black']
['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

"""


def main():
    lst = ['Red', 'Green', 'Blue', 'White', 'Black']
    print([_[::-1] for _ in lst])


if __name__ == "__main__":
    main()
