"""

Write a Python program to find the number of zeros at the end of a factorial of a given positive number.

Range of the number(n): (1 ≤ n ≤ 2*109).

    5   =>  1
    12  =>  2
    100 =>  24

"""

from math import factorial


def main():
    n = int(input("Enter a number: "))
    f = str(factorial(n))
    print(len(f) - len(f.rstrip("0")))


if __name__ == "__main__":
    main()
