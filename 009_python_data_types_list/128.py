"""

Write a Python program to calculate the sum of the numbers in a list between the indices of a specified range.

[2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
Range: 8 , 10

29

"""


def main():
    lst = [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
    print(sum(lst[8:11]))


if __name__ == "__main__":
    main()
