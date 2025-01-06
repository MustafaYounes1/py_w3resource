"""

Write a Python program to sum the missing numbers in a given list of integers.

[0, 3, 4, 7, 9]     -> 22
[44, 45, 48]        -> 93
[-7, -5, -4, 0]     -> -12

"""


def main():
    data = [
        [0, 3, 4, 7, 9],
        [44, 45, 48],
        [-7, -5, -4, 0]
    ]

    for lst in data:
        print(sum([_ for _ in range(min(lst), max(lst) + 1) if _ not in lst]))


if __name__ == "__main__":
    main()
