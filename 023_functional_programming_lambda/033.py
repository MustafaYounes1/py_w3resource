"""

Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a
minimum length using lambda.

7, W3resource   =>  True

"""

from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from typing import Callable


def main():
    f: Callable[[str, int], bool] = lambda s, ml: ((set(s) & set(ascii_lowercase) != set()) and
                                                   (set(s) & set(ascii_uppercase) != set()) and
                                                   (set(s) & set(digits)) != set()) and len(s) >= ml
    print(f("W3resource", 7))


if __name__ == "__main__":
    main()
