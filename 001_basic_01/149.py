"""

Write a Python function that takes a positive integer and returns the sum of the cube of all positive integers
smaller than the specified number.

"""


def cube_sum(i):
    if i == 2:
        return 1

    return (i - 1) ** 3 + cube_sum(i - 1)


def main():
    n = int(input("Enter a positive integer: "))
    print(cube_sum(n))


if __name__ == "__main__":
    main()
