"""

Write a Python program to find the maximum and minimum values in a set.

{2, 3, 5, 10, 15, 20}

Maximum =>  20
Minimum =>  2

"""


def main():
    s = {2, 3, 5, 10, 15, 20}
    print(f"Maximum: {max(s)}")
    print(f"Minimum: {min(s)}")


if __name__ == "__main__":
    main()
