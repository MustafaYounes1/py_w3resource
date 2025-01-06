"""

Write a Python program to convert a given list of dictionaries into a list of values corresponding to the specified key.

simpsons = [
    { 'name': 'Areeba', 'age': 8 },
    { 'name': 'Zachariah', 'age': 36 },
    { 'name': 'Caspar', 'age': 34 },
    { 'name': 'Presley', 'age': 10 }
]

Key = 'age'

[8, 36, 34, 10]

"""

from operator import itemgetter


def main():
    simpsons = [
        {'name': 'Areeba', 'age': 8},
        {'name': 'Zachariah', 'age': 36},
        {'name': 'Caspar', 'age': 34},
        {'name': 'Presley', 'age': 10}
    ]
    key = 'age'
    print(list(map(itemgetter(key), simpsons)))


if __name__ == "__main__":
    main()
