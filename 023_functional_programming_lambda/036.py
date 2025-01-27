"""

Write a Python program to extract the nth element from a given list of tuples using lambda.

[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]

Extract nth element ( n = 0 ) from the said list of tuples:
['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']

Extract nth element ( n = 2 ) from the said list of tuples:
[99, 96, 94, 98]

"""

from operator import itemgetter


def main():
    lst = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
    print(list(map(itemgetter(0), lst)))
    print(list(map(itemgetter(2), lst)))


if __name__ == "__main__":
    main()
