"""

Write a Python program to remove the parenthesis area in a string.

["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]

example
w3resource
github
stackoverflow

"""

import re


def main():
    lst = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
    pa = re.compile(r"\s?\(\.com\)")

    for _ in lst:
        print(pa.sub("", _))


if __name__ == "__main__":
    main()
