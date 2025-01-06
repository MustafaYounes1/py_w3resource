"""

Write a Python program to list the home directory without an absolute path.

"""

import pathlib


def main():
    for _ in pathlib.Path.home().iterdir():
        print(_)


if __name__ == "__main__":
    main()
