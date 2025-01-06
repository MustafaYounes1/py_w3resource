"""

Write a Python program to format a number with a percentage.

0.25    =>  25.00%
-0.25   =>  -25.00%

"""


def main():
    print(f"{0.25:.2%}")
    print(f"{-0.25:.2%}")


if __name__ == "__main__":
    main()
