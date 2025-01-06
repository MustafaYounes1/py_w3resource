"""

Write a Python program to split a multi-line string into a list of lines.

This
is a
multiline
string.

['This', 'is a', 'multiline', 'string.']

"""


def main():
    s = """This
is a
multiline
string."""

    print(s.split("\n"))


if __name__ == "__main__":
    main()
