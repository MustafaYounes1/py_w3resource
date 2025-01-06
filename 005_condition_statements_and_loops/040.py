"""

Write a Python program to find the median of three values.
Expected Output:

Input first number: 15
Input second number: 26
Input third number: 29
The median is 26.0

"""

from statistics import median


def main():
    n1, n2, n3 = list(map(int, input("Enter three white-separated integers: ").split()))
    print(median((n1, n2, n3)))


if __name__ == "__main__":
    main()
