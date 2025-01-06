"""

Write a Python program to check if a given function returns True for every element in a list.

[4, 2, 3], lambda x: x > 1  =>  True
[4, 2, 3], lambda x: x < 1  =>  False
[4, 2, 3], lambda x: x == 1 =>  False

"""


def main():
    data = [
        [[4, 2, 3], lambda x: x > 1],
        [[4, 2, 3], lambda x: x < 1],
        [[4, 2, 3], lambda x: x == 1]
    ]

    for lst, func in data:
        print(all(map(func, lst)))


if __name__ == "__main__":
    main()
