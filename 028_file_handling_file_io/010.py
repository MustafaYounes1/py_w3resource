"""

Write a Python program to get the file size of a plain file.
    Input file: 007.txt

0.71 KB

"""

import pathlib


__in_file_path = "007.txt"


def main():
    print(f"{pathlib.Path(__in_file_path).stat().st_size / 1024:.2f} KB")


if __name__ == "__main__":
    main()
