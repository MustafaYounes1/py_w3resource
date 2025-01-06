"""

Write a Python program to access the index of a list.

[5, 15, 35, 8, 98]

0 5
1 15
2 35
3 8
4 98

"""


def main():
    lst = [5, 15, 35, 8, 98]
    for idx, v in enumerate(lst):
        print(idx, v)


if __name__ == "__main__":
    main()
