"""

Given a list of numbers and a number to inject, write a Python program to create a list containing that number
in between each pair of adjacent numbers.

Input: [12, -7, 3, -89, 14, 88, -78, -1, 2, 7]
Separator: 6
Output:
[12, 6, -7, 6, 3, 6, -89, 6, 14, 6, 88, 6, -78, 6, -1, 6, 2, 6, 7]

Input: [1, 2, 3, 4, 5, 6]
Separator: 9
Output:
[1, 9, 2, 9, 3, 9, 4, 9, 5, 9, 6]

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    n = int(input("Enter the inject number: "))
    ans = [n] * (2 * len(seq) - 1)
    ans[::2] = seq
    print(ans)

if __name__ == "__main__":
    main()
