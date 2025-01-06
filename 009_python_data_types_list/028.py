"""

Write a Python program to find the second largest number in a list.

[1, 2, 3, 4, 4]                 =>  3
[1, 1, 1, 0, 0, 0, 2, -2, -2]   =>  1
[2, 2]                          =>  None
[1]                             =>  None

"""


def main():
    lists = [
        [1, 2, 3, 4, 4],
        [1, 1, 1, 0, 0, 0, 2, -2, -2],
        [2, 2],
        [1]
    ]

    for lst in lists:
        s = set(lst)
        if len(s) <= 1:
            print(None)
        else:
            print(sorted(s, reverse=True)[1])


if __name__ == "__main__":
    main()
