"""

Write a Python program to find the central character(s) of a given string. Return the two middle characters if the
length of the string is even. Return the middle character if the length of the string is odd.

Original string: Python         =>  th
Original string: PHP            =>  H
Original string: Java           =>  av

"""


def main():
    s = input("Enter a string: ")
    c = s[len(s) // 2] if len(s) % 2 != 0 else s[len(s) // 2 - 1: len(s) // 2 + 1]
    print(c)


if __name__ == "__main__":
    main()
