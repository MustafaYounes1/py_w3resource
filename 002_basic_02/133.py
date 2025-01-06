"""

Write a Python program to compute the sum of the negative and positive numbers in an array of integers and display the
largest sum.

Original array elements: {0, 15, 16, 17, -14, -13, -12, -11, -10, 18, 19, 20}   =>  105
Original array elements: {0, 3, 4, 5, 9, -22, -44, -11}                         =>  -77

"""


def find_largest(seq):
    sums = [0, 0]
    for _ in seq:
        if _ >= 0:
            sums[0] += _
        else:
            sums[1] += _

    if abs(sums[0]) > abs(sums[1]):
        return sums[0]
    else:
        return sums[1]


def main():
    seq = [int(_) for _ in input("Enter a list of space-separated integers: ").split(", ")]
    print(find_largest(seq))


if __name__ == "__main__":
    main()
