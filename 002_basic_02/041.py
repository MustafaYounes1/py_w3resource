"""

Write a Python program to compute and print the sum of two given integers (greater or equal to zero).
In the event that the given integers or the sum exceed 80 digits, print "overflow".
Input first integer:        25
Input second integer:       22
Sum of the two integers:    47

"""


def main():
    a, b = [int(_) for _ in input("Enter two space-separated integers: ").split()]
    res = a + b
    if res > 80:
        print("Overflow")
    else:
        print(res)


if __name__ == "__main__":
    main()
