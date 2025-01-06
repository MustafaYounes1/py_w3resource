"""

Write a Python program to print the following integers with '*' to the right of the specified width.

3   =>  3*
123 =>  123***

"""


def main():
    print(f"{3:*<2d}")
    print(f"{123:*<6d}")


if __name__ == "__main__":
    main()
