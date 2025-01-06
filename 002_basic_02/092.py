"""

 Write a Python program to compute the cumulative sum of numbers in a given list.
Note: Cumulative sum = sum of itself + all previous numbers in the said list.

Sample Input:
[10, 20, 30, 40, 50, 60, 7]     =>  [10, 30, 60, 100, 150, 210, 217]
[1, 2, 3, 4, 5]                 =>  [1, 3, 6, 10, 15]
[0, 1, 2, 3, 4, 5]              =>  [0, 1, 3, 6, 10, 15]

"""


def main():
    seq = list(map(int, input("Enter a list of space-separated integers: ").split()))

    res = [
        sum(seq[:_ + 1]) for _ in range(len(seq))
    ]

    print(res)


if __name__ == "__main__":
    main()
