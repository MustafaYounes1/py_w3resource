"""

Write a Python program to sum all numerical values (positive integers) embedded in a sentence.

Input:
Sentences with positive integers are given over multiple lines. Each line is a character string containing one-byte
alphanumeric characters, symbols, spaces, or an empty line. However the input is 80 characters or less per line and
the sum is 10,000 or less.

Sum of the numeric values:                      "sd1fdsfs23 dssd56"           80
Sum of the numeric values:                      "15apple2banana"              17
Sum of the numeric values:                      "flowers5fruit5"              10

"""

import re


def main():
    s = input("Input the string: ")
    print(sum([int(_) for _ in re.findall(r"[0-9]+", s)]))


if __name__ == "__main__":
    main()
