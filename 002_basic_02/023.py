"""

Write a Python program that accepts a positive number and subtracts from it the sum of its digits, and so on.

Continue this operation while the number is positive.

    9       => 0
    20      => 0
    110     => 0
    5674    => 0

"""


def find_sub(n):
    while n > 0:
        n -= sum([int(_) for _ in str(n)])

    return n


def main():
    n = int(input("Enter a number: "))
    print(find_sub(n))


if __name__ == "__main__":
    main()
