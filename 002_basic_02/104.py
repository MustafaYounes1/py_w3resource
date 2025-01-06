"""

Write a Python program to find a number in a given matrix that is maximum in its column and minimum in its row.

Sample Input:
Original matrix: [[1, 2], [2, 3]]                   =>  2
Original matrix: [[1, 2, 3], [3, 4, 5]]             =>  3
Original matrix: [[7, 5, 6], [3, 4, 4], [6, 5, 7]]  =>  5

"""


def main():
    n_rows = int(input("Enter the number of rows: "))

    data = [
        list(map(int, input("").split())) for _ in range(n_rows)
    ]

    results = set(map(min, data)) & set(map(max, zip(*data)))

    print(results)


if __name__ == "__main__":
    main()
