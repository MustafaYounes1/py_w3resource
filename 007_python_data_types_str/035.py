"""

Write a Python program to display a number with a comma separator.

1           =>  1
3000000     =>  3,000,000
30000000    =>  30,000,000

"""


def main():
    print(f"{1:,}")
    print(f"{3000000:,}")
    print(f"{30000000:,}")


if __name__ == "__main__":
    main()
