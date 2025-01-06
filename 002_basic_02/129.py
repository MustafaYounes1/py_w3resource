"""

Write a Python program to get the index number of all lower case letters in a given string.

Original string: Python         =>  [1, 2, 3, 4, 5]
Original string: JavaScript     =>  [1, 2, 3, 5, 6, 7, 8, 9]
Original string: PHP            =>  []

"""


def main():
    s = input("Enter a string: ")
    print([idx for idx, _ in enumerate(s) if _.islower()])


if __name__ == "__main__":
    main()
