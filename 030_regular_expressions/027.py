"""

Write a Python program to separate and print the numbers in a given string.

"Ten 10, Twenty 20, Thirty 30"      =>  [10, 20, 30]

"""

import re


def main():
    s = "Ten 10, Twenty 20, Thirty 30"
    print(list(map(int, re.findall(r"\d+", s))))


if __name__ == "__main__":
    main()
