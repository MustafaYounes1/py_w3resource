"""

Write a Python program to get the size of a file.

"""

import pathlib


def main():
    file_path = pathlib.Path(input("Enter the file path: "))
    assert file_path.is_file(), f"{file_path} is not a path to a file!"
    print(f"{file_path.stat().st_size / 1024:.2f} Kb")


if __name__ == "__main__":
    main()
