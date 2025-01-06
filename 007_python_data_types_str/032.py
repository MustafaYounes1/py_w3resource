"""

Write a Python program to print the following positive and negative numbers with no decimal places.

3.1415926   =>  +3
-12.9999    =>  -13

"""


def main():
    print(f"{3.1415926:+.0f}")
    print(f"{-12.9999:+.0f}")


if __name__ == "__main__":
    main()
