"""

Write a Python program to find files and skip directories in a given directory.

"""

import pathlib


def main():
    path = pathlib.Path(input("Enter a path to a directory: "))
    assert path.is_dir(), f"{path} is not a directory"

    for _ in path.iterdir():
        if _.is_file():
            print(_)


if __name__ == "__main__":
    main()
