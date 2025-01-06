"""

Write a Python program to sort all python files in an input directory by the modification date.

"""

# finds all the path names matching a specified pattern according to the rules used by the Unix shell
from glob import glob
import pathlib


def main():
    d = pathlib.Path(input("Enter the input directory: "))
    assert d.is_dir(), f"{d} does not exist"
    py_files = glob(str(d / "*.py"))
    py_files = sorted(py_files, key=lambda x: pathlib.Path(x).stat().st_mtime)
    for _ in py_files:
        print(_)


if __name__ == "__main__":
    main()
