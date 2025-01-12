"""

Write a Python program to find the third-largest number from a given list of numbers.
Note: Use the Python set data type.

[1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 10]    =>  8
[1, 2, 3, 4, 5, 6, 7, 8, 9]                 =>  7
[1, 2, 3]                                   =>  1
[1, 2, 2]                                   =>  None
[1, 2]                                      =>  None

"""

from heapq import nlargest


def main():
    data = [
        [1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 10],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3],
        [1, 2, 2],
        [1, 2],
    ]

    for lst in data:
        largest_3 = nlargest(3, set(lst))
        if len(largest_3) == 3:
            print(largest_3[-1])
        else:
            print(None)


if __name__ == "__main__":
    main()
