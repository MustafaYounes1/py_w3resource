"""

Write a Python program to decapitalize the first letter of a given string.

Java Script     =>  java Script
Python          =>  python

"""


def main():
    s = input("Enter a string: ")
    words = s.split()
    print(" ".join([words[0].lower()] + words[1:]))


if __name__ == "__main__":
    main()
