"""

Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda.

[[1, 2, 3], [2, 4, 5], [1, 1, 1]]       =>  [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]    =>  [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]

"""


def main():
    data = [
        [[1, 2, 3], [2, 4, 5], [1, 1, 1]],
        [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
    ]

    for lst in data:
        print(sorted(lst, key=sum))


if __name__ == "__main__":
    main()
