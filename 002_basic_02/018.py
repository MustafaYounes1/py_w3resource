"""

Write a Python program to find the median among three given numbers.

"""

from statistics import median


def main():
    a, b, c = [int(_) for _ in input("Enter three space-separated integers: ").split()]
    print(median([a, b, c]))


if __name__ == "__main__":
    main()
