"""

Write a Python program to create a flat list of all the values in a flat dictionary.

{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

[19, 20, 21, 20]

"""


def main():
    d = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
    print(list(d.values()))


if __name__ == "__main__":
    main()
