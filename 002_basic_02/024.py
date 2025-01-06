"""

Write a Python program to find the total number of even or odd divisors of a given integer.

    15      =>  4
    12      =>  6
    9       =>  3
    6       =>  4
    3       =>  2

"""


def main():
    n = int(input("Enter a number: "))
    divisors = [_ for _ in range(1, n + 1) if n % _ == 0]
    print(len(divisors))


if __name__ == "__main__":
    main()
