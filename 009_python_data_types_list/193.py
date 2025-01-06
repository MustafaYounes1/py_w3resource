"""

Write a Python program to find the dimension of a given matrix.

[[1, 2], [2, 4]]                    =>  (2, 2)
[[0, 1, 2], [2, 4, 5]]              =>  (2, 3)
[[0, 1, 2], [2, 4, 5], [2, 3, 4]]   =>  (3, 3)

"""


def main():
    data = [
        [[1, 2], [2, 4]],
        [[0, 1, 2], [2, 4, 5]],
        [[0, 1, 2], [2, 4, 5], [2, 3, 4]]
    ]

    for mat in data:
        print((len(mat), max(len(_) for _ in mat)))


if __name__ == "__main__":
    main()
