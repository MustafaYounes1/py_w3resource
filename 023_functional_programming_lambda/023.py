"""

Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using the

[2, 4, -6, -9, 11, -12, 14, -5, 17]

Sum of the positive numbers: -32
Sum of the negative numbers: 48

"""


def main():
    lst = [2, 4, -6, -9, 11, -12, 14, -5, 17]
    print(sum(filter(lambda _: _ < 0, lst)))
    print(sum(filter(lambda _: _ >= 0, lst)))


if __name__ == "__main__":
    main()
