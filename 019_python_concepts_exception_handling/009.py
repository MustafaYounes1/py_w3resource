"""

Write a Python program that opens a file (009.txt) with ASCII decoding and handles a UnicodeDecodeError exception
if there is an encoding issue.

"""

import pathlib


def main():
    try:
        with open(pathlib.Path("009.txt"), 'r', encoding="ASCII") as f:
            print("".join(f.readlines()))

    except FileNotFoundError as e:
        print(e)

    except UnicodeDecodeError as e:
        print(e)


if __name__ == "__main__":
    main()
