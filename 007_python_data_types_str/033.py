"""

Write a Python program to print the following integers with zeros to the left of the specified width.

3       =>  03
123     =>  000123

"""


def main():
    print(f"{3:0>2d}")
    print(f"{123:0>6d}")


if __name__ == "__main__":
    main()
