"""

Write a Python program to swap cases in a given string.

Python Exercises    =>  pYTHON eXERCISES

"""


def main():
    s = input("Enter a string: ")
    print("".join([_.upper() if _.islower() else _.lower() for _ in s]))


if __name__ == "__main__":
    main()
