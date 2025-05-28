"""

Write a Python program that converts a hexadecimal string into a bytes sequence.

4861636b657220436f6465  =>  b'Hacker Code'

"""


def main():
    print(bytes.fromhex("48 61 63 6b 65 72 20 43 6f 64 65"))


if __name__ == "__main__":
    main()
