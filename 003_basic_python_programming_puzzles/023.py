"""

Write a Python program to find the indices at which the numbers in the list drop.
NOTE: You can detect multiple drops just by checking if nums[i] < nums[i-1]

Input:
[0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
Output:
[1, 4, 6, 8, 10, 11, 15, 16, 18]

Input:
[6, 5, 4, 3, 2, 1]
Output:
[1, 2, 3, 4, 5]

Input:
[1, 19, 5, 15, 5, 25, 5]
Output:
[2, 4, 6]

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(", ")))

    print(
        [i + 1 for i in range(len(seq) - 1) if seq[i + 1] < seq[i]]
    )


if __name__ == "__main__":
    main()
