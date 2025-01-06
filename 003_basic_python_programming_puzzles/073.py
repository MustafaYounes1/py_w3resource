"""

Write a Python program to find a substring in a given string that contains a vowel between two consonants.

Input: Hello        =>  Hel
Input: Sandwhich    =>  San
Input: Python       =>  hon

"""

import re

__data = [
    "Hello",
    "Sandwhich",
    "Python",
    "muu"
]


def main():
    for s in __data:
        # pattern: consonant|vowel|consonant
        # use [^...] to exclude a set of characters when matching
        print(re.findall(r"[^aeiouAEIOU][aeiouAEIOU][^aeiouAEIOU]", s))


if __name__ == "__main__":
    main()
