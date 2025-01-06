"""

Write a Python program to get a string from a given string where all occurrences of its first char have been
 changed to '$', except the first char itself.

Sample String : 'restart'
Expected Result : 'resta$t'

"""


def main():
    s = input("Enter a string: ")
    print(s[0] + s[1:].replace(s[0], "$"))


if __name__ == "__main__":
    main()
