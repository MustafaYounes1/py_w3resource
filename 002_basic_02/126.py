"""

Write a Python program to convert the letters of a given string (same case-upper/lower) into alphabetical order.

Original string: PHP            =>  HPP
Original string: javascript     =>  aacijprstv
Original string: python         =>  hnopty

"""

from string import ascii_lowercase, ascii_uppercase


def main():
    s = input("Enter a string: ")
    print(
        "".join(sorted(s))
    )


if __name__ == "__main__":
    main()
