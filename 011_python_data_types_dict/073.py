"""

Write a Python program to convert a list of dictionaries into a list of values corresponding to the specified key.

[
    {'name': 'Theodore', 'age': 18},
    {'name': 'Mathew', 'age': 22},
    {'name': 'Roxanne', 'age': 20},
    {'name': 'David', 'age': 18}
]

'age'   =>  [18, 22, 20, 18]

"""

from operator import itemgetter


def main():
    data = [
        {'name': 'Theodore', 'age': 18},
        {'name': 'Mathew', 'age': 22},
        {'name': 'Roxanne', 'age': 20},
        {'name': 'David', 'age': 18}
    ]
    key = 'age'

    print(list(map(itemgetter(key), data)))


if __name__ == "__main__":
    main()
