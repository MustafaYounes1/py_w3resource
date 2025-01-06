"""

A Python list contains some positive integers. Write a Python program to count the numbers that are greater than
the previous number on the list.

Sample Data:
([1, 4, 7, 9, 11, 5]) -> 4
([1, 3, 3, 2, 2]) -> 1
([4, 3, 2, 1]) -> 0

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated numbers: ").split(", ")))
    print(
        len(
            [(i1, i2) for i1, i2 in zip(seq, seq[1:]) if i2 > i1]
        )
    )


if __name__ == "__main__":
    main()
