"""

Write a Python function to merge a list of lists into one sorted list.

[[1, 4, 5], [1, 3, 4], [2, 6, 7, 8]]    =>  [1, 1, 2, 3, 4, 4, 5, 6, 7, 8]
[[1, 2], [-1, -2, -3], [0]]             =>  [-3, -2, -1, 0, 1, 2]

"""

from heapq import merge


def main():
    data = [
        [[1, 4, 5], [1, 3, 4], [2, 6, 7, 8]],
        [[1, 2], [-1, -2, -3], [0]]
    ]

    for lst in data:
        print(list(merge(*map(sorted, lst))))


if __name__ == "__main__":
    main()
