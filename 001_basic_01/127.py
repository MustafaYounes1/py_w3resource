"""

Write a Python program to check whether an integer fits in 64 bits.

"""


def main():
    i = int(input("Enter an integer: "))
    print(i.bit_length() <= 64)


if __name__ == "__main__":
    main()
