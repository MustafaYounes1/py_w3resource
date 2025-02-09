"""

Write a Python program that matches a word at the beginning of a string.

The quick brown fox jumps over the lazy dog.    =>  The

"""

import re


def main():
    s = "The quick brown fox jumps over the lazy dog."
    print(re.match(r"\w+", s).group())


if __name__ == "__main__":
    main()
