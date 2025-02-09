"""

Write a Python program that matches a word containing 'z'.

The quick brown fox jumps over the lazy dog.    =>  True
Python Exercises.                               =>  False

"""

import re


def main():
    data = ["The quick brown fox jumps over the lazy dog.", "Python Exercises."]
    pa = re.compile(r"\w*z\w*")
    for _ in data:
        print(pa.search(_) is not None)


if __name__ == "__main__":
    main()
