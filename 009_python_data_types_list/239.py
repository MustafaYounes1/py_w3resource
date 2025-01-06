"""

Write a Python program to find the value of the first element in the given list that satisfies the provided
testing function.

[1, 2, 3, 4], lambda n: n % 2 == 1      =>  1
[1, 2, 3, 4], lambda n: n % 2 == 0      =>  2

"""


def main():
    data = [
        [[1, 2, 3, 4], lambda n: n % 2 == 1],
        [[1, 2, 3, 4], lambda n: n % 2 == 0]
    ]

    for lst, func in data:
        print(next(_ for _ in lst if func(_)))


if __name__ == "__main__":
    main()
