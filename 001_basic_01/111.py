"""

Write a Python program to make file lists from the current directory using a wildcard.

e.g. List all python files that start with '00' in the current directory.

"""

import glob


def main():
    py_files = glob.glob("./00*.py")
    print("\n".join(py_files))


if __name__ == "__main__":
    main()
