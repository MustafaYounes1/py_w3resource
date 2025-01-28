"""

Write a Python program that will select a specified number of colours from three different colours, and then generate
all the combinations with repetitions.

["Red", "Green", "Blue"]

1: [('Red',), ('Green',), ('Blue',)]

2: [('Red', 'Red'), ('Red', 'Green'), ('Red', 'Blue'), ('Green', 'Green'), ('Green', 'Blue'), ('Blue', 'Blue')]

3: [
    ('Red', 'Red', 'Red'), ('Red', 'Red', 'Green'), ('Red', 'Red', 'Blue'), ('Red', 'Green', 'Green'),
    ('Red', 'Green', 'Blue'), ('Red', 'Blue', 'Blue'), ('Green', 'Green', 'Green'), ('Green', 'Green', 'Blue'),
    ('Green', 'Blue', 'Blue'), ('Blue', 'Blue', 'Blue')
]

"""

from itertools import combinations_with_replacement


def main():
    lst = ["Red", "Green", "Blue"]
    print(list(combinations_with_replacement(lst, 1)))
    print(list(combinations_with_replacement(lst, 2)))
    print(list(combinations_with_replacement(lst, 3)))


if __name__ == "__main__":
    main()
