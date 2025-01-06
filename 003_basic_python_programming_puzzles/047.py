"""

Write a Python program to filter for numbers in a given list whose sum of digits is > 0, where the first digit can
be negative.

Input:
[11, -6, -103, -200]
Output:
[11, -103]

Input:
[1, 7, -4, 4, -9, 2]
Output:
[1, 7, 4, 2]

Input:
[10, -11, -71, -13, 14, -32]
Output:
[10, -13, 14]

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    print(
        [n for n in seq if int(str(n)[:2]) + sum(map(int, str(n)[2:])) > 0]
    )


if __name__ == "__main__":
    main()
