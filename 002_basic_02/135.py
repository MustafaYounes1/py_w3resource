"""

Write a Python program that calculates the Least Common Multiple (LCM) of more than two numbers. The numbers should be
taken from a given list of positive integers.
From Wikipedia,
In arithmetic and number theory, the least common multiple, lowest common multiple, or smallest common multiple of two
integers a and b, usually denoted by lcm(a, b), is the smallest positive integer that is divisible by both a and b.
Since division of integers by zero is undefined, this definition has meaning only if a and b are both different from
zero. However, some authors define lcm(a,0) as 0 for all a, which is the result of taking the lcm to be the least
upper bound in the lattice of divisibility.

Original list elements: [4, 6, 8]                           =>  24
Original list elements: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     =>  2520
Original list elements: [48, 72, 108]                       =>  432

"""

from math import lcm


# Define a function 'gcd' that calculates the Greatest Common Divisor (GCD) of two numbers.
def gcd_from_scratch(a, b):
    # Use the Euclidean algorithm to find the GCD of 'a' and 'b'.
    while b:
        a, b = b, a % b
    return a


# Define a function 'lcm' that calculates the Least Common Multiple (LCM) of two numbers.
def lcm_from_scratch(a, b):
    # Calculate the LCM using the formula: LCM(a, b) = (a * b) / GCD(a, b).
    return a * b // gcd_from_scratch(a, b)


def main():
    seq = [int(_) for _ in input("Enter a list of space-separated numbers: ").split(", ")]
    print(lcm(*seq))


if __name__ == "__main__":
    main()
