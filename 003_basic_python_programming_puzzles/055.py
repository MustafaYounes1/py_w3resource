"""

Write a Python program to find numbers that are greater than 10 and have odd first and last digits.

Input:
[1, 3, 79, 10, 4, 1, 39, 62]
Output:
[79, 39]

Input:
[11, 31, 77, 93, 48, 1, 57]
Output:
[11, 31, 77, 93, 57]

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    print(
        [_ for _ in seq if _ > 10 and int(str(_)[0]) % 2 != 0 and int(str(_)[-1]) % 2 != 0]
    )


if __name__ == "__main__":
    main()
