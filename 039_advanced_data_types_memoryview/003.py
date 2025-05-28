"""

Write a Python program that creates a list from a memory view over the following bytes object b'\x03\x02\x01CBA'.

->  [3, 2, 1, 67, 66, 65]

"""


def main():
    b = b'\x03\x02\x01CBA'
    print(memoryview(b).tolist())


if __name__ == "__main__":
    main()
