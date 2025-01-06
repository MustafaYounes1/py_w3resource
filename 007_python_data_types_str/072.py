"""

Write a Python program to remove all characters except a specified character from a given string.

Python Exercises,   P   =>  P

google,             g   =>  gg

exercises,          e   =>  eee

"""


def main():
    s, k = input("Enter the string and the set of characters as two comma-separated strings: ").split(", ")
    print("".join([_ for _ in s if _ in k]))


if __name__ == "__main__":
    main()
