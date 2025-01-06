"""

Write a Python program to find the common values that appear in two given strings.

Original strings:
Python3, Python2.7

Intersection of two said String:
Python

"""

from difflib import SequenceMatcher


def main():
    s1, s2 = input("Enter the two strings comma-separated: ").split(", ")
    matcher = SequenceMatcher(None, s1, s2)
    longest_match = matcher.find_longest_match(0, len(s1), 0, len(s2))
    print(s1[longest_match.a: longest_match.size])


if __name__ == "__main__":
    main()
