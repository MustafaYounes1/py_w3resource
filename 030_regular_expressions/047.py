"""

Write a Python program to split a string with multiple delimiters.
    Possible delimiters: [; , \n *]

The quick brown\nfox jumps*over the lazy dog.    =>  ['The quick brown', 'fox jumps', 'over the lazy dog.']

"""

import re


def main():
    s = "The quick brown\nfox jumps*over the lazy dog."
    print(re.split(r"[;,\n*]", s))


if __name__ == "__main__":
    main()
