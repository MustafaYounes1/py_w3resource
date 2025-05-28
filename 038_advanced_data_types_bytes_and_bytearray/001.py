"""

Write a Python program to convert a given string to bytes using different encodings like UTF-8, UTF-16, ASCII etc.

"Python Exercises!"

ASCII   b'Python Exercises!'
UTF-8   b'Python Exercises!'
UTF-16  b'\xff\xfeP\x00y\x00t\x00h\x00o\x00n\x00 \x00E\x00x\x00e\x00r\x00c\x00i\x00s\x00e\x00s\x00!\x00'

"""


def main():
    s = f"Python Exercises!"
    print(f"ASCII:  {s.encode('ascii', errors='replace')}")
    print(f"UTF-8:  {s.encode('utf-8', errors='replace')}")
    print(f"UTF-16: {s.encode('utf-16', errors='replace')}")


if __name__ == "__main__":
    main()
