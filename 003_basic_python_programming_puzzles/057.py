"""

Write a Python program to find the sum of the magnitudes of the elements in the array.
This sum should have a sign that is equal to the product of the signs of the entries.

[1, 3, -2]          =>  -6
[1, -3, 3]          =>  -7
[10, 32, 3]         =>  45
[-25, -12, -23]     =>  -60

"""

from math import prod


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    abs_sum = sum([abs(_) for _ in seq])
    print(
        1 * abs_sum if prod(seq) >= 0 else -1 * abs_sum
    )


if __name__ == "__main__":
    main()
