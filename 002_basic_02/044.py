"""

Write a Python program to find the maximum sum of a contiguous subsequence from a given sequence of numbers
a1, a2, a3, .... A subsequence of one element is also a continuous subsequence.

Input:
You can assume that 1 <= n <= 5000 and -100000 <= ai <= 100000.
Input numbers are separated by a space.
Input 0 to exit.
Input number of sequence of numbers you want to input (0 to exit):  3
Input numbers:
2
4
6
Maximum sum of the said contiguous subsequence: 12
Input number of sequence of numbers you want to input (0 to exit):
0

"""


def main():
    n = int(input("Input number of sequence of numbers you want to input (0 to exit): "))
    res = 0
    for _ in range(n):
        tmp = int(input(""))
        if tmp == 0:
            break
        res += tmp

    print(res)


if __name__ == "__main__":
    main()
