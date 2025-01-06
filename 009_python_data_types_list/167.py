"""

Write a Python program to convert a given list of strings into a list of lists.

['Red', 'Maroon', 'Yellow', 'Olive']

[['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]

"""


def main():
    lst = ['Red', 'Maroon', 'Yellow', 'Olive']
    print([list(_) for _ in lst])


if __name__ == "__main__":
    main()
