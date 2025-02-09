"""

Write a Python program to find all words that are at least 4 characters long in a string.

"The quick brown fox jumps over the lazy dog."  =>  ['quick', 'brown', 'jumps', 'over', 'lazy']

"""

import re


def main():
    s = "The quick brown fox jumps over the lazy dog."
    print(re.findall(r"\b\w{4,}\b", s))


if __name__ == "__main__":
    main()
