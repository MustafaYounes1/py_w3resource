"""

Write a Python program that takes a positive integer and calculates the cube root of the number until the number
is less than three. Count the number of steps to complete the task.

Sample Data:
(3) -> 1
(39) -> 2
(10000) -> 2

"""

from math import cbrt


def main():
    n = int(input("Enter a number: "))
    steps = 0

    while n >= 3:
        n = cbrt(n)
        steps += 1

    print(steps)


if __name__ == "__main__":
    main()
