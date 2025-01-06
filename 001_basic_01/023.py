"""

Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string.
Return n copies of the whole string if the length is less than 2.

"""


def main():
    string = input("Enter the string: ")
    n = int(input("Enter the number of copies: "))
    if len(string) < 2:
        print(string * n)
    else:
        print(string[:2] * n)


if __name__ == "__main__":
    main()
