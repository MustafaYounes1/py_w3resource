"""

Write a Python program to convert a given Bytearray to a Hexadecimal string.

Original Bytearray :
[111, 12, 45, 67, 109]

Hexadecimal string:
6f0c2d436d

"""


def main():
    lst = [111, 12, 45, 67, 109]
    print("".join([f"{_:02x}" for _ in lst]))


if __name__ == "__main__":
    main()
