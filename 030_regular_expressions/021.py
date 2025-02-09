"""

Write a Python program to find the number of occurrences of a substrings within a string.

Sample text :   'Python exercises, PHP exercises, C# exercises'

Pattern :       'exercises'     =>  3 matches

"""

import re


def main():
    s = "Python exercises, PHP exercises, C# exercises"
    pa = "exercises"
    print(len(re.findall(rf"{pa}", s)))


if __name__ == "__main__":
    main()
