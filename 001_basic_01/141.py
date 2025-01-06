"""

Write a python program to convert decimal to hexadecimal.
    Sample decimal number: 30, 4
    Expected output: 1e, 04

"""


def main():
    for d in [30, 4]:
        print(f"{d:02x}")


if __name__ == "__main__":
    main()
