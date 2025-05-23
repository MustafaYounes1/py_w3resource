"""

Write a Python program to find the largest and smallest digits of a given number.

Original Number: 9387422
Largest Digit of the said number: 9
Smallest Digit of the said number: 2

Original Number: 500
Largest Digit of the said number: 5
Smallest Digit of the said number: 0

Original Number: 231548
Largest Digit of the said number: 8
Smallest Digit of the said number: 1

"""


def main():
    n = input("Enter a number: ")
    digits = list(map(int, n))
    print(max(digits), min(digits))


if __name__ == "__main__":
    main()
