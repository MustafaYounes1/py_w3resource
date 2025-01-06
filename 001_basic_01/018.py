"""

Write a Python program to calculate the sum of three given numbers.
If the values are equal, return three times their sum.

"""


def main():
    numbers = [int(_) for _ in input("Enter 3 comma-separated numbers: ").split(",")]
    if len(set(numbers)) == 1:
        print(sum(numbers) * 3)
    else:
        print(sum(numbers))


if __name__ == "__main__":
    main()
