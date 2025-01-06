"""

Write a Python program to check the validity of passwords input by users.
Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.

"""

import re


def main():
    p = input("Enter a password: ")

    if not re.search("[a-z]", p):
        print("Not valid, At least 1 letter between [a-z]")

    elif not re.search("[A-Z]", p):
        print("Not valid, At least 1 letter between [A-Z]")

    elif not re.search("[0-9]", p):
        print("Not valid, At least 1 letter between [0-9]")

    elif not re.search("[$#@]", p):
        print("Not valid, At least 1 letter in [$#@]")

    elif not (6 <= len(p) <= 16):
        print("Not valid, len should be in the range: [6, 16]")

    else:
        print("Valid")


if __name__ == "__main__":
    main()
