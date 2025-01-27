"""

Write a Python program to find if a given string starts with 'P' using Lambda.

Python  =>  True
Java    =>  False

"""

from typing import Callable


def main():
    f: Callable[[str], bool] = lambda s: s.startswith('P')
    print(f("Python"))
    print(f("Java"))


if __name__ == "__main__":
    main()
