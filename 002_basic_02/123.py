"""

Write a Python program to remove the first and last elements from a given string.

Original string: PHP        =>  H
Original string: Python     =>  ytho
Original string: JavaScript =>  avaScrip

"""


def main():
    s = input("Enter a string: ")
    print(s[1:-1])


if __name__ == "__main__":
    main()
