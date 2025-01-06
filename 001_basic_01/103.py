"""

Write a Python program to extract the filename from a given path.

"""

import pathlib


def main():
    file_abs_path = pathlib.Path(input("Enter the absolute path to a file: "))
    assert file_abs_path.is_absolute(), f"{file_abs_path} is not an absolute path"
    assert file_abs_path.is_file(), f"{file_abs_path} is not a file"
    print(file_abs_path.name)


if __name__ == "__main__":
    main()
