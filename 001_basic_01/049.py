"""

Write a Python program to list all files in a directory.

"""

import os
import pathlib


def main():
    d = input("Enter a directory: ")

    # using os
    print([_ for _ in os.listdir(d) if os.path.isfile(os.path.join(d, _))])

    print("=" * 15)

    # using pathlib
    for _ in pathlib.Path(d).iterdir():
        if _.is_file():
            print(str(_))


if __name__ == "__main__":
    main()
