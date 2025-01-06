"""

Write a Python program that capitalizes the first letter and lowercases the remaining letters in a given string.

Red Green WHITE                 -> "Red Green White"
w3resource                      -> "W3resource"
dow jones industrial average    -> "Dow Jones Industrial Average"

"""


def main():
    s = input("Enter a string: ")
    print(" ".join([_.capitalize() for _ in s.split()]))


if __name__ == "__main__":
    main()
