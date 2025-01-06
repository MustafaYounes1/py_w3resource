"""

Write a Python program to find the second smallest number in a list.

[1, 2, -8, -2, 0, -2]       =>  2
[1, 1, 0, 0, 2, -2, -2]     =>  0
[2, 2]                      =>  None
[2]                         =>  None

"""


def main():
    lists = [
        [1, 2, -8, -2, 0, -2],
        [1, 1, 0, 0, 2, -2, -2],
        [2, 2],
        [2]
    ]

    for lst in lists:
        s = set(lst)
        if len(s) <= 1:
            print(None)
        else:
            print(sorted(s)[1])


if __name__ == "__main__":
    main()
