"""

Write a Python program that accepts a filename from the user and prints the extension of the file.

Sample filename : abc.java
Output : java

"""

import pathlib


def main():
    filename = input("Enter a filename (name.ext): ")
    print(pathlib.Path(filename).suffix[1:])


if __name__ == "__main__":
    main()
