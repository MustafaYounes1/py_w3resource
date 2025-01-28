"""

Write a Python program to create an iterator that returns consecutive keys and groups from an iterable.

'AAAAJJJJHHHHNWWWEERRRSSSOOIIU'
    [
        ('A', ['A', 'A', 'A', 'A']), ('J', ['J', 'J', 'J', 'J']), ('H', ['H', 'H', 'H', 'H']), ('N', ['N']),
        ('W', ['W', 'W', 'W']), ('E', ['E', 'E']), ('R', ['R', 'R', 'R']), ('S', ['S', 'S', 'S']), ('O', ['O', 'O']),
        ('I', ['I', 'I']), ('U', ['U'])
    ]

[1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 8]
    [(1, [1]), (2, [2, 2]), (3, [3]), (4, [4, 4]), (5, [5, 5, 5]), (6, [6, 6]), (7, [7, 7, 7]), (8, [8])]

"""

from itertools import groupby


def main():
    data = [
        'AAAAJJJJHHHHNWWWEERRRSSSOOIIU',
        [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 8]
    ]

    for _ in data:
        print([(k, list(g)) for k, g in groupby(_)])


if __name__ == "__main__":
    main()
