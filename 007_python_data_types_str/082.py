"""

Write a Python program to wrap a given string into a paragraph with a given width.

Sample Output:
Input a string: The quick brown fox.
Input the width of the paragraph: 10

Result:
The quick
brown fox.

"""

import textwrap


def main():
    s = input("Enter a string: ")
    print(textwrap.fill(s, 10))


if __name__ == "__main__":
    main()
