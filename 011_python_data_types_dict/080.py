"""

Write a Python program to find the key of the maximum/minimum value in a dictionary.

{'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}

('Roxanne', 'Theodore')

"""


def main():
    d = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
    print((max(d, key=d.get), min(d, key=d.get)))


if __name__ == "__main__":
    main()
