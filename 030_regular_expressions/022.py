"""

Write a Python program to find the occurrence and position of substrings within a string.

string:     Python exercises, PHP exercises, C# exercises
pattern:    exercises

7:16
22:31
36:45

"""

import re


def main():
    s = "Python exercises, PHP exercises, C# exercises"
    pa = "exercises"

    for ma in re.finditer(rf"{pa}", s):
        print(":".join(map(str, ma.span())))


if __name__ == "__main__":
    main()
