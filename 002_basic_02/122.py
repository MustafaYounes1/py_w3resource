"""

Write a Python program to check if a given string contains only lowercase or uppercase characters.

Original string: PHP            =>  True
Original string: javascript     =>  True
Original string: JavaScript     =>  False

"""


def main():
    s = input("Enter a string: ")
    print(s.islower() or s.isupper())


if __name__ == "__main__":
    main()
