"""

Write a Python program to calculate the value of 'a' to the power of 'b' using recursion.

Test Data :
(power(3,4) -> 81

"""


def power(a, b):
    if b == 0:
        return 1

    return a * power(a, b - 1)


def main():
    n1, n2 = 3, 4
    print(power(n1, n2))


if __name__ == "__main__":
    main()
