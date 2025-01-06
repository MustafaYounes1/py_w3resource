"""

Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0)
using recursion.

Test Data:
sum_series(6) -> 12
sum_series(10) -> 30

"""


def sum_seq(n):
    if n <= 0:
        return 0

    else:
        return n + sum_seq(n - 2)


def main():
    n = int(input("Enter a number: "))
    print(sum_seq(n))

if __name__ == "__main__":
    main()
