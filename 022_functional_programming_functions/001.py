"""

Write a Python function to find the maximum of three numbers.

3, 6, -5        =>  6

"""


def maximum(a: int | float, b: int | float, c: int | float) -> int | float:
    return max(a, b, c)


def main():
    print(maximum(3, 6, -5))


if __name__ == "__main__":
    main()
