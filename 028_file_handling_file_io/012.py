"""

Write a Python program to copy the contents of a file to another file.
    Input file: 001.txt
    Output file: 012.txt

"""

import shutil


__in_file_path = "001.txt"
__out_file_path = "012.txt"


def main():
    shutil.copyfile(__in_file_path, __out_file_path)


if __name__ == "__main__":
    main()
