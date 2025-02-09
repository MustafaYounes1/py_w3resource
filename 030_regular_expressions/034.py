"""

Write a Python program to find all three, four, and five character words in a string.

"The quick brown fox jumps over the lazy dog."

['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

"""

import re


def main():
    s = "The quick brown fox jumps over the lazy dog."
    print(re.findall(r"\b\w{3,5}\b", s))


if __name__ == "__main__":
    main()
