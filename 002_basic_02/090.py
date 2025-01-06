"""

Write a Python program that replaces all but the last five characters of a string with "*" and returns the modified
string.

Original String: kdi39323swe    =>  ******23swe

Original String: 12345abcdef    =>  ******bcdef

Original String: 12345          =>  12345

"""


def modify(s):
    return '*' * (len(s) - 5) + s[-5:]


def main():
    s = input("Enter a string: ")
    print(modify(s))


if __name__ == "__main__":
    main()
