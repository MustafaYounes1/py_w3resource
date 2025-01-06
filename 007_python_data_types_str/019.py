"""

Write a Python program to get the last part of a string before a specified character.

https://www.w3resource.com/python-exercises     '-'

https://www.w3resource.com/python

"""


def main():
    s = input("Enter a string: ")
    c = input("Enter a char: ")
    print(s.rsplit(c, maxsplit=1)[0])


if __name__ == "__main__":
    main()
