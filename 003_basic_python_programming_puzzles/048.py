"""

Write a Python program to find the indices of two entries that show that the list is not in increasing order.
If there are no violations (they are increasing), return an empty list.

[1, 2, 3, 0, 4, 5, 6]       =>  [2, 3]
[1, 2, 3, 4, 5, 6]          =>  []
[1, 2, 3, 4, 6, 5, 7]       =>  [4, 5]
[-3, -2, -3, 0, 2, 3, 4]    =>  [1, 2]

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    print(
        [(idx - 1, idx) for idx in range(1, len(seq)) if seq[idx-1] > seq[idx]]
    )


if __name__ == "__main__":
    main()
