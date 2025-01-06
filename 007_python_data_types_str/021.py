"""

Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase
characters in the first 4 characters.

Python  =>  Python
PyThon  =>  PYTHON

"""


def main():
    s = input("Enter a string: ")

    if len(list(filter(lambda x: x.isupper(), s[:4]))) >= 2:
        print(s.upper())
    else:
        print(s)


if __name__ == "__main__":
    main()
