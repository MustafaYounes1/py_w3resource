"""

Write a Python program to reverse a given string in lower case.

Original string: PHP        =>  php
Original string: JavaScript =>  tpircsavaj
Original string: PHPP       =>  pphp

"""


def main():
    s = input("Enter a string: ")
    print(s[::-1].lower())


if __name__ == "__main__":
    main()
