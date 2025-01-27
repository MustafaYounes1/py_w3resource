"""

Write a Python program to extract a specified size of strings from a given list of string values using lambda.

8, ['Python', 'list', 'exercises', 'practice', 'solution']  =>  ['practice', 'solution']

"""


def main():
    s, lst = 8, ['Python', 'list', 'exercises', 'practice', 'solution']
    print(list(filter(lambda _: len(_) == s, lst)))


if __name__ == "__main__":
    main()
