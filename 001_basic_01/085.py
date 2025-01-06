"""

Write a Python program to check whether a file path is a file or a directory.

"""

import pathlib


def main():
    path = pathlib.Path(input("Enter your path: "))
    if path.is_file():
        print(f"{path} is a file")
    elif path.is_dir():
        print(f"{path} is a directory")
    else:
        print(f"{path} is neither a path nor a directory")


if __name__ == "__main__":
    main()
