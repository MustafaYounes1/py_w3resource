"""

Write a Python program to find the largest product of a pair of adjacent elements from a given list of integers.

Original list: [1, 2, 3, 4, 5, 6]   =>  30
Original list: [1, 2, 3, 4, 5]      =>  20
Original list: [2, 3]               =>  6

"""


def main():
    seq = list(map(int, input("Enter a list of space-separated numbers: ").split()))

    m = max(a * b for a, b in zip(seq, seq[1:]))
    print(m)


if __name__ == "__main__":
    main()
