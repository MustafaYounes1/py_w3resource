"""

Write a Python program to get the absolute file path of an input relative path.

"""

import pathlib


def main():
    rel_path = pathlib.Path(input("Enter the relative path: "))
    assert rel_path.is_file(), f"{rel_path} does not exist"
    print(rel_path.absolute())


if __name__ == "__main__":
    main()
