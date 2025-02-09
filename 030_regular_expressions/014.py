"""

Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

The quick brown fox jumps over the lazy dog.    =>  False
Python_Exercises_1                              =>  True

"""

import re


def main():
    data = ["The quick brown fox jumps over the lazy dog.", "Python_Exercises_1"]
    pa = re.compile(r"\w+$")
    for _ in data:
        print(pa.match(_) is not None)


if __name__ == "__main__":
    main()
