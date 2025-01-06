"""

Write a Python program to remove duplicates from a list of integers, preserving order.

Input:
[1, 3, 4, 10, 4, 1, 43]
Output:
[1, 3, 4, 10, 43]

Input:
[10, 11, 13, 23, 11, 25, 23, 76, 99]
Output:
[10, 11, 13, 23, 25, 76, 99]

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    distinct = set()
    res = []
    for _ in seq:
        if _ not in distinct:
            res.append(_)
            distinct.add(_)

    print(res)


if __name__ == "__main__":
    main()
