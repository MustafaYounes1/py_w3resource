"""

Write a Python program to find x that minimizes the mean squared deviation from a given list of numbers.
(Hint: Find x as the mean)

Input:
[4, -5, 17, -9, 14, 108, -9]
Output:
17.142857142857142

Input:
[12, -2, 14, 3, -15, 10, -45, 3, 30]
Output:
1.1111111111111112

"""

from statistics import mean


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    print(mean(seq))


if __name__ == "__main__":
    main()
