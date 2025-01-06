"""

Write a Python program to find all index positions of the maximum and minimum values in a given list of numbers.

[12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]

Index positions of the maximum value of the said list:
7

Index positions of the minimum value of the said list:
3, 11

"""


def main():
    lst = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
    ma = max(lst)
    mi = min(lst)
    print(" ".join([str(idx) for idx, _ in enumerate(lst) if _ == ma]))
    print(" ".join([str(idx) for idx, _ in enumerate(lst) if _ == mi]))


if __name__ == "__main__":
    main()
