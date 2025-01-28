"""

Write a Python program to get all possible combinations of the elements of a given list using the itertools module.

['orange', 'red', 'green', 'blue']

[
    [()],
    [('orange',), ('red',), ('green',), ('blue',)],
    [('orange', 'red'), ('orange', 'green'), ('orange', 'blue'), ('red', 'green'), ('red', 'blue'), ('green', 'blue')],
    [('orange', 'red', 'green'), ('orange', 'red', 'blue'), ('orange', 'green', 'blue'), ('red', 'green', 'blue')],
    [('orange', 'red', 'green', 'blue')]
]

"""

from itertools import combinations


def main():
    lst = ['orange', 'red', 'green', 'blue']
    print([list(combinations(lst, i)) for i in range(len(lst) + 1)])


if __name__ == "__main__":
    main()
