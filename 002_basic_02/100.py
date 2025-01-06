"""

Write a Python program to compute the sum of all items in a given array of integers where each integer is multiplied
by its index. Return 0 if there is no number.

Sample Input:
[1,2,3,4]       =>  20
[-1,-2,-3,-4]   =>  -20
[]              =>  0

"""


def main():
    seq = list(map(int, input("Enter a list of space-separated integers: ").split()))
    print(
        sum(
            [_ * idx for _, idx in enumerate(seq)]
        )
    )


if __name__ == "__main__":
    main()
