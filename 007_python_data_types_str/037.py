"""

Write a Python program to display a number in left, right, and center aligned with a width of 10.

"""


def main():
    print(f"Center: {22:^10d}")
    print(f"Left  : {22:<10d}")
    print(f"Right : {22:>10d}")


if __name__ == "__main__":
    main()
