"""

Write a Python program to sort a list of lists by a given index of the inner list using lambda.

[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]

Sort the said list of lists by a given index ( Index = 0 ) of the inner list
[('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99), ('Wyatt Knott', 91, 94)]

Sort the said list of lists by a given index ( Index = 2 ) of the inner list
[('Wyatt Knott', 91, 94), ('Brady Kent', 97, 96), ('Beau Turnbull', 94, 98), ('Greyson Fulton', 98, 99)]

"""

from operator import itemgetter


def main():
    lst = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
    print(sorted(lst, key=itemgetter(0)))
    print(sorted(lst, key=itemgetter(2)))

if __name__ == "__main__":
    main()
