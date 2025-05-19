"""

Write a Python program that implements a function to check if a given string is a valid email address format using
boolean logic.

Accepted format: "firstName_SecondName@gmail.com"

"foo_bar@gmail.com"     =>  True
"foo_bar2@gmail.com"    =>  False
"foo2@gmail.com"        =>  False
"foo2@x.com"            =>  False

"""

import re

_email_pa = re.compile(r"^[a-zA-Z]+_[a-zA-Z]+@gmail.com$")


def is_valid(s: str) -> bool:
    return _email_pa.match(s) is not None


def main():
    data = [
        "foo_bar@gmail.com",
        "foo_bar2@gmail.com",
        "foo2@gmail.com",
        "foo2@x.com",
    ]

    for _ in data:
        print(is_valid(_))


if __name__ == "__main__":
    main()
