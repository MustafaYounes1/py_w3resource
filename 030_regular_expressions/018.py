"""

Write a Python program to search for numbers (0-9) of length between 1 and 3 in a given string.

"Exercises number 1, 12, 13, and 345 are important, but 9999 does not exist"     =>  [1, 12, 13, 345]

"""

import re


def main():
    s = "Exercises number 1, 12, 13, and 345 are important"
    print(list(map(int, re.findall(r"\d{1,3}", s))))


if __name__ == "__main__":
    main()
