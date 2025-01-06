"""

Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of
ones of same length in a given string. Return True/False.

    Original sequence: 01010101
    True

    Original sequence: 00
    False

    Original sequence: 000111000111
    True

    Original sequence: 00011100011
    False

"""


def main():
    string = input("Enter a string: ")

    while "01" in string:
        string = string.replace("01", "")

    print(len(string) == 0)


if __name__ == "__main__":
    main()
