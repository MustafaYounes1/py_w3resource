"""

Write a Python program that matches a word containing 'z', not the start or end of the word.

lazy    =>  True
buz     =>  False
Python  =>  False
zoo     =>  False

"""

import re


def main():
    data = ["lazy", "buz", "Python", "zoo"]
    pa = re.compile(r"\Bz\B")
    for _ in data:
        print(pa.search(_) is not None)


if __name__ == "__main__":
    main()
