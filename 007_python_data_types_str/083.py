"""

Write a Python program to print four integer values - decimal, octal, hexadecimal (capitalized),
binary - in a single line.

Sample Output:
Input an integer: 25
Decimal Octal Hexadecimal (capitalized), Binary
25 31 19 11001

"""


def main():
    n = 25
    print(f"{n:d} {n:o} {n:x} {n:b}")


if __name__ == "__main__":
    main()
