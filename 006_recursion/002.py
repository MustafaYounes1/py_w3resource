"""

Write a Python program to convert an integer to a string in any base using recursion.

integer: 2835, base: 16     =>  B13

"""


def to_string(n, base):

    cvt_string = '0123456789ABCDEF'

    if n < base:
        return cvt_string[n]

    else:
        return to_string(n // base, base) + cvt_string[n % base]


def main():
    n = 2835
    base = 16
    print(to_string(2835, 16))


if __name__ == "__main__":
    main()
