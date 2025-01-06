"""

Write a Python program that accepts a list of numbers. Count the negative numbers and compute the sum of the positive
numbers of the said list. Return these values through a list.

Original list: [1, 2, 3, 4, 5]
Number of negative of numbers and sum of the positive numbers of the said list: [0, 15]

Original list: [-1, -2, -3, -4, -5]
Number of negative of numbers and sum of the positive numbers of the said list: [5, 0]

Original list: [1, 2, 3, -4, -5]
Number of negative of numbers and sum of the positive numbers of the said list: [2, 6]

Original list: [1, 2, -3, -4, -5]
Number of negative of numbers and sum of the positive numbers of the said list: [3, 3]

"""


def main():
    seq = list(map(int, input("Enter a list of space-separated integers: ").split()))
    print([
        len([_ for _ in seq if _ < 0]),
        sum([_ for _ in seq if _ > 0])
    ])


if __name__ == "__main__":
    main()
