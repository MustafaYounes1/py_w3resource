"""

Write a python program to find the longest word.
    Input file: 007.txt
    Note: clear all punctuations except for "-"

general-purpose

"""

from itertools import chain
from string import punctuation


__in_file_path = "007.txt"


def main():
    with open(__in_file_path, "r") as f:
        lines = list(map(lambda _: _.strip("\n"), f.readlines()))
        s = set(chain(*[line.split() for line in lines]))
        s = set(map(lambda _: _.translate(str.maketrans("", "", punctuation.replace("-", ""))), s))
        print(max(s, key=len))


if __name__ == "__main__":
    main()
