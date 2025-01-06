"""

Write a Python program to get a directory listing, sorted by creation date.

"""

import pathlib


def main():
    d = pathlib.Path(input("Enter the input directory: "))
    assert d.is_dir(), f"{d} does not exist"
    files = list(d.iterdir())
    py_files = sorted(files, key=lambda x: x.stat().st_ctime)
    for _ in py_files:
        print(_)


if __name__ == "__main__":
    main()
