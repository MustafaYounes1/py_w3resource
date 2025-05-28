"""

Write a Python program that slices of a memory view over b'\x01\x02\x03\x04\x05\x06\x07\x08\t\n'

Note: print the decimal representation of the bytes starting from the fourth byte to the eighth byte
    ->  [4, 5, 6, 7, 8]

"""


def main():
    mv = memoryview(b'\x01\x02\x03\x04\x05\x06\x07\x08\t\n')
    print(mv[3:8].tolist())


if __name__ == "__main__":
    main()
