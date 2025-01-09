"""

Write a Python program to find all keys in a dictionary that have the given value.

d = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
val = 20

['Roxanne', 'Betty']

"""


def main():
    d = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
    val = 20
    print(list(filter(lambda _: d.get(_) == val, d)))


if __name__ == "__main__":
    main()
