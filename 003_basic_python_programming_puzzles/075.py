"""

Write a Python program to reorder numbers from a given array in increasing/decreasing order based on whether the
first plus last element is odd/even.

Odd     => increasing
Even    => decreasing

[3, 7, 4]               =>  [3, 4, 7]
[2, 7, 4]               =>  [7, 4, 2]
[1, 5, 6, 7, 4, 2, 8]   =>  [1, 2, 4, 5, 6, 7, 8]
[1, 5, 6, 7, 4, 2, 9]   =>  [9, 7, 6, 5, 4, 2, 1]

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    print(
        sorted(
            seq,
            reverse=(seq[0] + seq[-1]) % 2 == 0
        )
    )


if __name__ == "__main__":
    main()
