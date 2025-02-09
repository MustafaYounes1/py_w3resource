"""

Write a Python program to check for a number at the end of a string.

abcdef  =>  False
abcdef6 =>  True

"""

import re


def main():
    data = ["abcdef", "abcdef6"]
    pa = re.compile(r"\d$")
    for _ in data:
        print(pa.search(_) is not None)


if __name__ == "__main__":
    main()
