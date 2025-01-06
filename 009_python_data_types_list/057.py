"""

Write a Python program to check if all items in a given list of strings are equal to a given string.

["green", "orange", "black", "white"], 'blue'   =>  False
["green", "green", "green", "green"], 'green'   =>  True

"""


def main():
    lst, s = ["green", "green", "green", "green"], 'green'
    print(all(_ == s for _ in lst))


if __name__ == "__main__":
    main()
