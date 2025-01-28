"""

Write a Python program to find all lower and upper mixed case combinations of a given string.

abc
['abc', 'abC', 'aBc', 'aBC', 'Abc', 'AbC', 'ABc', 'ABC']

w3r
['w3r', 'w3R', 'w3r', 'w3R', 'W3r', 'W3R', 'W3r', 'W3R']

"""

from itertools import product


def main():
    data = ("abc", "w3r")
    for _ in data:
        print(list(map("".join, product(*map(lambda __: (__.lower(), __.upper()), _)))))

if __name__ == "__main__":
    main()
