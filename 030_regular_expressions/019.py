"""

Write a Python program to search for literal strings within a string.

'The quick brown fox jumps over the lazy dog.'

'fox'       =>  True
'dog'       =>  True
'horse'     =>  False

"""

import re


def main():
    s = "The quick brown fox jumps over the lazy dog."
    words = ["fox", "dog", "horse"]
    for w in words:
        print(re.search(rf"\b{w}\b", s) is not None)


if __name__ == "__main__":
    main()
