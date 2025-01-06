"""

Write a Python program to compute the digit number of the sum of two given integers.
Each test case consists of two non-negative integers x and y which are separated by a space in a line.
0 <= x, y <= 1,000,000

Input two integers(a b):        5 7
Sum of two integers a and b.:   2   (two digits 12)

"""


def main():
    a, b = [int(_) for _ in input("Enter two space-separated integers: ").split()]
    print(len(str(a+b)))


if __name__ == "__main__":
    main()
