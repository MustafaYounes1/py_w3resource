"""

Write a Python program to convert an integer to binary that keeps leading zeros.

    Sample data : x=12
    Expected output : 00001100

"""


def main():
    x = 12
    print(f"{x:08b}")


if __name__ == "__main__":
    main()
