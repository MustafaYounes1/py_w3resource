"""

Write a Python program to find the maximum length of consecutive 0's in a given binary string.

111000010000110     =>  4
111000111           =>  3

"""

import re


def main():
    s = input("Enter a binary string: ")
    print(len(max(re.findall("0+", s), key=len)))
    # or
    # print(len(max(s.split("1"), key=len)))

if __name__ == "__main__":
    main()
