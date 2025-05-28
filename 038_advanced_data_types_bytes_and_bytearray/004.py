"""

Write a Python program that reads an input file into a bytes object and saves a modified copy.

Note: Read the "004.txt" file and write the following bytes in it:
    [10, 104, 101, 108, 108, 111, 32, 119, 51, 114, 101, 115, 111, 117, 114, 99, 101, 33]

"""

from pathlib import Path


def main():
    input_file = Path("004.txt")
    assert input_file.is_file(), f"{input_file} doesn't exist"

    bytes_lst = [10, 104, 101, 108, 108, 111, 32, 119, 51, 114, 101, 115, 111, 117, 114, 99, 101, 33]
    bytes_ = input_file.read_bytes()
    input_file.write_bytes(bytes_ + bytes(bytes_lst))


if __name__ == "__main__":
    main()
