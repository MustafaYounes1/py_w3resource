"""

Write a Python program to remove all duplicates from a given list of strings and return a list of unique strings.
Note: Use the Python set data type.

['foo', 'bar', 'abc', 'foo', 'qux', 'bar', 'baz']               =>  ['bar', 'qux', 'abc', 'baz', 'foo']
['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']    =>  ['Practice', 'Exercises', 'Python', 'Solution']

"""


def main():
    data = [
        ['foo', 'bar', 'abc', 'foo', 'qux', 'bar', 'baz'],
        ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
    ]

    for lst in data:
        print(list(set(lst)))


if __name__ == "__main__":
    main()
