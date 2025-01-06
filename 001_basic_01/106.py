"""

Write a Python program to divide a path by the extension separator.

"""

import pathlib


def main():
    file_path = pathlib.Path(input("Enter a path to a file: "))
    print(file_path.parent / file_path.stem)
    print(file_path.suffix)


if __name__ == "__main__":
    main()
