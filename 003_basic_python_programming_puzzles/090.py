"""

For each triple of eaten, need, and stock, write a Python program to get a pair of total appetite and remaining.

[[2, 5, 6], [3, 9, 22]]                                         =>  [[7, 1], [12, 13]]
[[2, 3, 18], [4, 9, 2], [2, 5, 7], [3, 8, 12], [4, 9, 106]]     =>  [[5, 15], [6, 0], [7, 2], [11, 4], [13, 97]]
[[1, 2, 3], [4, 5, 6]]                                          =>  [[3, 1], [9, 1]]

"""


__data = [
    [[2, 5, 6], [3, 9, 22]],
    [[2, 3, 18], [4, 9, 2], [2, 5, 7], [3, 8, 12], [4, 9, 106]],
    [[1, 2, 3], [4, 5, 6]]
]


def main():
    for sample in __data:
        print([[a + min(b, c), max(0, c - b)] for a, b, c in sample])


if __name__ == "__main__":
    main()
