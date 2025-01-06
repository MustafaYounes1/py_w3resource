"""

Write a Python program to find the largest k numbers from a given list of numbers.

Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]      k = 1
Output:
[6]

Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]      k = 2
Output:
[6, 5]

Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]      k = 3
Output:
[6, 5, 5]

Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]      k = 4
Output:
[6, 5, 5, 4]

Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]      k = 5
Output:
[6, 5, 5, 4, 3]

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    k = int(input("Enter k: "))
    print(sorted(seq, reverse=True)[:k])


if __name__ == "__main__":
    main()
