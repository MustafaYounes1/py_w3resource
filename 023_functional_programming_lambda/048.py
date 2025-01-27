"""

Write a Python program to count the occurrences of items in a given list using lambda.

[3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
{0: 2, 1: 1, 2: 2, 3: 4, 4: 2, 5: 3, 8: 2}

"""


def main():
    lst = [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
    print(dict(map(lambda _: (_, lst.count(_)), set(lst))))


if __name__ == "__main__":
    main()
