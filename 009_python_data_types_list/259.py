"""

Write a Python program to check if a given function returns True for at least one element in the list.

[1, 0, 2, 3], lambda x: x >= 3  =>  True
[1, 0, 2, 3], lambda x: x < 0   =>  False
[2, 2, 4, 4], lambda x: x       =>  True

"""


def main():
    data = [
        [[1, 0, 2, 3], lambda x: x >= 3],
        [[1, 0, 2, 3], lambda x: x < 0],
        [[2, 2, 4, 4], lambda x: x]
    ]

    for lst, func in data:
        print(any(map(func, lst)))


if __name__ == "__main__":
    main()
