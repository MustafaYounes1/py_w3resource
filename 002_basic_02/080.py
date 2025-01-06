"""

Write a Python program to find the first missing positive integer that does not exist in a given list.

Sample Input:
[2, 3, 7, 6, 8, -1, -10, 15, 16]    =>  4
[1, 2, 4, -7, 6, 8, 1, -10, 15]     =>  3
[1, 2, 3, 4, 5, 6, 7]               =>  8
[-2, -3, -1, 1, 2, 3]               =>  4

"""

from sys import maxsize


def main():
    seq = list(map(int, input("Enter a list of space-separated integers: ").split()))

    min_pos = sorted([_ for _ in seq if _ > 0])[0]
    for _ in range(min_pos, maxsize):
        if _ not in seq:
            print(_)
            break


if __name__ == "__main__":
    main()
