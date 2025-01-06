"""

Write a Python program to check if a given function returns True for at least one element in the list.

[0, 1, 2, 0], lambda x: x >= 2      =>  True
[5, 10, 20, 10], lambda x: x < 2    =>  False

"""


def main():
    data = [
        [[0, 1, 2, 0], lambda x: x >= 2 ],
        [[5, 10, 20, 10], lambda x: x < 2]
    ]

    for lst, func in data:
        print(any(map(func, lst)))


if __name__ == "__main__":
    main()
