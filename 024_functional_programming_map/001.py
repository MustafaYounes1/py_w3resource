"""

Write a Python program to triple all numbers in a given list of integers. Use Python map.

[1, 2, 3, 4, 5, 6, 7]   =>  [3, 6, 9, 12, 15, 18, 21]

"""


def main():
    lst = [1, 2, 3, 4, 5, 6, 7]
    print(list(map(lambda _: _ * 3, lst)))


if __name__ == "__main__":
    main()
