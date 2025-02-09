"""

Write a Python program to find all five-character words in a string.

"The quick brown fox jumps over the lazy dog."   =>  ['quick', 'brown', 'jumps']

"""

import re


def main():
    s = "The quick brown fox jumps over the lazy dog."
    print(re.findall(r"\b\w{5}\b", s))


if __name__ == "__main__":
    main()
