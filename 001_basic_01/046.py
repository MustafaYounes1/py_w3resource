"""

Write a Python program to retrieve the path and name of the file currently being executed.

"""

import pathlib


def main():
    cur_file = pathlib.Path(__file__)
    print(f"path: {cur_file.parent}")
    print(f"name: {cur_file.name}")


if __name__ == "__main__":
    main()
