"""

Write a Python program to print this Unicode character "2713" (the checkmark).

Unicode (https://www.unicode.org/) is a specification that aims to list every character used by human languages
and give each character its own unique code.

see: https://docs.python.org/3/howto/unicode.html

"""

import string


def main():
    print("here is your checkmark: " + u'\u2713')


if __name__ == "__main__":
    main()
