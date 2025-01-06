"""

Write a Python program to remove duplicate words from a given list of strings.

['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']

['Python', 'Exercises', 'Practice', 'Solution']

"""

from itertools import groupby


def main():
    lst = ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
    print([k for k, _ in groupby(sorted(lst))])


if __name__ == "__main__":
    main()
