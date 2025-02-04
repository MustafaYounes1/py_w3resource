"""

Write a Python program to read a random line from a file.
    Input file: 001.txt

"""

import random

__in_file_path = "001.txt"


def main():
    random.seed(0)

    with open(__in_file_path, "r") as f:
        lines = f.read().splitlines(keepends=False)
        print(random.choice(lines))


if __name__ == "__main__":
    main()
