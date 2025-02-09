"""

Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

ABCDEFabcdef123450      =>  True
ABCDEFabcdef123450_     =>  False
ABCDEFabc!def123450     =>  False
*&%@#!}{                =>  False

"""

import re


def main():
    data = ["ABCDEFabcdef123450", "ABCDEFabcdef123450_", "ABCDEFabc!def123450", "*&%@#!}{"]
    pa = re.compile(r"[^a-zA-Z0-9]")
    for _ in data:
        print(pa.search(_) is None)


if __name__ == "__main__":
    main()
