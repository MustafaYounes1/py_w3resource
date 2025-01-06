"""

Write a Python program to extract specified size of strings from a give list of string values.

['Python', 'list', 'exercises', 'practice', 'solution'], 8

['practice', 'solution']

"""


def main():
    lst, ll = ['Python', 'list', 'exercises', 'practice', 'solution'], 8
    print(list(filter(lambda _: len(_) == ll, lst)))


if __name__ == "__main__":
    main()
