"""

Write a Python program that matches a string of two letters (a, b) that starts with an "a" followed by zero or more "b"s.

ac      =>  False
abc     =>  False
a       =>  True
ab      =>  True
abb     =>  True

"""

import re


def main():
    data = ["ac", "abc", "a", "ab", "abb"]
    pa = re.compile(r"ab*$")
    for _ in data:
        print(pa.match(_) is not None)


if __name__ == "__main__":
    main()
