"""

Write a Python program to find the starting and ending position of a given value in an array of integers,
sorted in ascending order.

If the target is not found in the array, return [-1, 0].
Input: [5, 7, 7, 8, 8, 8] target value = 8      =>  Output: [3, 5]
Input: [1, 3, 6, 9, 13, 14] target value = 4    =>  Output: [-1, 0]

"""


def main():
    seq = list(map(int, input("Enter a list of space-separated integers: ").split()))
    n = int(input("Enter the integer: "))

    try:
        i0 = seq.index(n)
        i1 = len(seq) - 1 - seq[-1::-1].index(n)

    except ValueError:
        i0, i1 = -1, 0

    print([i0, i1])


if __name__ == "__main__":
    main()
