"""

Write a Python program to check whether lowercase letters exist in a string.

"""

import string


def main():
    s = input("Enter a string: ")
    print(len(set(s) & set(string.ascii_lowercase)) > 0)


if __name__ == "__main__":
    main()
