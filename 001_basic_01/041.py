"""

Write a Python program to check whether a file exists.

"""

import pathlib


def main():
    p = input("Enter the file path: ")
    if pathlib.Path(p).is_file():
        print(f"{p} exists")
    else:
        print(f"{p} does not exist")


if __name__ == "__main__":
    main()
