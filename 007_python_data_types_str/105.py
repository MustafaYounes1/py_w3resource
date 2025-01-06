"""

Write a Python program to extract and display the name from a given Email address.

john@example.com                    -> ("john")
john.smith@example.com              -> ("johnsmith")
fully-qualified-domain@example.com  -> ("fullyqualifieddomain")

"""

import re
from string import digits, punctuation


def main():
    s = input("Enter a string: ")
    match = re.match(r".+@", s).group()
    cleaned = match.translate(str.maketrans("", "", digits + punctuation))
    print(cleaned)


if __name__ == "__main__":
    main()
