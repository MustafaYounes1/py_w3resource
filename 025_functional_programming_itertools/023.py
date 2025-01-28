"""

Write a Python program to find the maximum length of a substring in a given string where all the characters of the
substring are the same. Use the itertools module to solve the problem.

"aaabbccddeeeee"    =>  5
"c++ exercises"     =>  2

"""

from itertools import groupby


def main():
    data = ["aaabbccddeeeee", "c++ exercises"]
    for _ in data:
        print(max([len(list(g)) for __, g in groupby(_)]))


if __name__ == "__main__":
    main()
