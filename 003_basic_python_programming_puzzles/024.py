"""

Write a Python program to create a list whose ith element is the maximum of the first i elements from an input list.

Input:
[0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
Output:
[0, 0, 3, 8, 8, 9, 9, 14, 14, 14, 14, 14, 14, 17, 41, 41, 41, 41, 41, 41]

Input:
[6, 5, 4, 3, 2, 1]
Output:
[6, 6, 6, 6, 6, 6]

Input:
[1, 19, 5, 15, 5, 25, 5]
Output:
[1, 19, 19, 19, 19, 25, 25]

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(", ")))
    print(
        [max(seq[: i + 1]) for i in range(0, len(seq))]
    )


if __name__ == "__main__":
    main()
