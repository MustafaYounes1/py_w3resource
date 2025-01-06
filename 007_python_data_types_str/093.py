"""

Write a Python program to extract numbers from a given string.

Original string: red 12 black 45 green
Extract numbers from the said string: [12, 45]

"""

import re


def main():
    s = input("Enter a string: ")
    print(re.findall("[0-9]+", s))


if __name__ == "__main__":
    main()
