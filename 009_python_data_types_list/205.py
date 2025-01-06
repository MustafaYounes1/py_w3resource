"""

Write a Python program to find the indices of elements in a given list that are greater than a specified value.

[1234, 1522, 1984, 19372, 1000, 2342, 7626]

3000    =>  [3, 6]
20000   =>  []

"""


def main():
    lst = [1234, 1522, 1984, 19372, 1000, 2342, 7626]
    nums = (3_000, 20_000)

    for n in nums:
        print([idx for idx, _ in enumerate(lst) if _ > n])


if __name__ == "__main__":
    main()
