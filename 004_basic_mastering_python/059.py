"""

Sort a list of dictionaries by a key.

lst = [{'name': 'Anej', 'age': 25}, {'name': 'Matteo', 'age': 22}, {'name': 'Eliza', 'age': 28}]
key: 'age'

[{'name': 'Matteo', 'age': 22}, {'name': 'Anej', 'age': 25}, {'name': 'Eliza', 'age': 28}]

"""


def main():
    lst = [{'name': 'Anej', 'age': 25}, {'name': 'Matteo', 'age': 22}, {'name': 'Eliza', 'age': 28}]
    key = 'age'
    print(sorted(lst, key=lambda d: d[key]))


if __name__ == "__main__":
    main()
