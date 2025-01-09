"""

Write a Python program to create a flat list of all the keys in a flat dictionary.

{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

['Theodore', 'Roxanne', 'Mathew', 'Betty']

"""


def main():
    d = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
    print(list(d.keys()))


if __name__ == "__main__":
    main()
