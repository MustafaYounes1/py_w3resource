"""

Write a Python function that searches for a bytes sequence within a file opened in byte mode.

Note: Get the index of the exclamation mark in the "004.txt" file
    -> 11

"""

from pathlib import Path


def main():
    input_file = Path("004.txt")
    assert input_file.is_file(), f"{input_file} doesn't exist"

    bytes_ = input_file.read_bytes()
    print(bytes_.find(b"!"))


if __name__ == "__main__":
    main()
