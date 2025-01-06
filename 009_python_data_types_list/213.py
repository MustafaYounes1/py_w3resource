"""

Write a Python program to calculate the sum of two lowest negative numbers in a given array of integers.

[-14, 15, -10, -11, -12, -13, 16, 17, 18, 19, 20]       =>  -27
[-4, 5, -2, 0, 3, -1, 4, 9]                             =>  -6

"""


def main():
    data = [
        [-14, 15, -10, -11, -12, -13, 16, 17, 18, 19, 20],
        [-4, 5, -2, 0, 3, -1, 4, 9]
    ]

    for lst in data:
        print(sum(sorted(lst)[:2]))


if __name__ == "__main__":
    main()
