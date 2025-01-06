"""

Write a Python program to generate and print a list of the first and last 5 elements where the values are square
numbers between 1 and 30 (both included).

[1, 4, 9, 16, 25]
[256, 289, 324, 361, 400]

"""


def main():
    lst = [pow(_, 2) for _ in range(1, 21)]
    print(lst[:5])
    print(lst[-5:])


if __name__ == "__main__":
    main()
