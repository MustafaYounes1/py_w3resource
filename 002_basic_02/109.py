"""

Write a Python program to find the indices of all occurrences of a given item in a given list.

Sample Input:
([1,2,3,4,5,2], 2)          =>  [1, 5]
([3,1,2,3,4,5,6,3,3], 3)    =>  [0, 3, 7, 8]
([1,2,3,-4,5,2,-4], -4)     =>  [3, 6]
([1, 2, 3, 4, 5, 2], 7)     =>  []

"""


def main():
    seq = list(map(int, input("Enter a list of space-separated integers: ").split()))
    n = int(input("Enter the number: "))

    print(
        [idx for idx, _ in enumerate(seq) if _ == n]
    )


if __name__ == "__main__":
    main()
