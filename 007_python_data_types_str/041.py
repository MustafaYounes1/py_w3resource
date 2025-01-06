"""

Write a Python program to strip a set of characters from a string.

The quick brown fox jumps over the lazy dog.    ,   aeiou
Th qck brwn fx jmps vr th lzy dg.
"""


def main():
    s = "The quick brown fox jumps over the lazy dog."
    chars = "aeiou"
    print(s.translate(str.maketrans("", "", chars)))


if __name__ == "__main__":
    main()
