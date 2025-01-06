"""

 Write a Python program to find the product of the units digits in the numbers in a given list.

Note: The Unit Place Digit refers to the digit placed in the one's position of the particular number. It is the
rightmost digit of the given number. For example, the unit place digit of the number 457 is 7.

[12, 23]        =>  6
[12, 23, 43]    =>  18
[113, 234]      =>  12
[1002, 2005]    =>  10

"""

from math import prod


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    # Python’s eval() allows you to evaluate arbitrary Python expressions from a string-based or
    # compiled-code-based input.
    print(
        eval('*'.join([str(x % 10) for x in seq]))
    )


if __name__ == "__main__":
    main()
