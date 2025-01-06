"""

Write a Python program to rotate a given list by a specified number of items in the right or left direction.

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'left', 4   =>  [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
'left', 2   =>  [3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
'right', 4  =>  [7, 8, 9, 10, 1, 2, 3, 4, 5, 6],
'right', 2  =>  [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]

"""


def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    rotations = [
        ['left', 4],
        ['left', 2],
        ['right', 4],
        ['right', 2]
    ]

    for d, s in rotations:
        if d == 'left':
            print(lst[s:] + lst[:s])
        else:
            print(lst[-s:] + lst[:-s])


if __name__ == "__main__":
    main()
