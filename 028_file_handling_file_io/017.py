"""

Write a Python program that takes a text file as input and returns the number of words of a given text file.
    Input file: 007.txt
    Note: clear all punctuations except for "-"

102

"""

from itertools import chain
from string import punctuation

__in_file_path = "007.txt"


def main():
    with open(__in_file_path, "r") as f:
        lines = f.read().splitlines(keepends=False)
        words = list(
            map(
                lambda word: word.translate(str.maketrans("", "", punctuation.replace("-", ""))),
                chain(*[line.split() for line in lines])
            )
        )
        print(len(words))


if __name__ == "__main__":
    main()
