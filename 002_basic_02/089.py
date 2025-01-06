"""

Write a Python program to compute the sum of the three lowest positive numbers from a given list of numbers.

Original list of numbers: [10, 20, 30, 40, 50, 60, 7]
Sum of the three lowest positive numbers of the said array: 37

Original list of numbers: [1, 2, 3, 4, 5]
Sum of the three lowest positive numbers of the said array: 6

Original list of numbers: [0, 1, 2, 3, 4, 5]
Sum of the three lowest positive numbers of the said array: 6

"""


def main():
    seq = list(map(int, input("Enter a list of space-separated integers: ").split()))
    print(sum(sorted([_ for _ in seq if _ > 0])[:3]))


if __name__ == "__main__":
    main()
