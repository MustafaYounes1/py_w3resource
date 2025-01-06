"""

Write a Python program to check whether a given sequence is linear, quadratic or cubic.

Sequences are sets of numbers that are connected in some way.

Linear sequence:
A number pattern which increases or decreases by the same amount each time is called a linear sequence.
The amount it increases or decreases by is known as the common difference.
[First differences between consecutive elements are the same]

Quadratic sequence:
In quadratic sequence, the difference between each term increases, or decreases, at a constant rate.
[Second differences between consecutive elements are the same]

Cubic sequence:
Sequences where the 3rd difference are known as cubic sequence.
[Third differences between consecutive elements are the same]

Sample Output:
Original Sequence: [0, 2, 4, 6, 8, 10]          =>  Linear Sequence

Original Sequence: [1, 4, 9, 16, 25]            =>  Quadratic Sequence

Original Sequence: [0, 12, 10, 0, -12, -20]     =>  Cubic Sequence

Original Sequence: [1, 2, 3, 4, 5]              =>  Linear Sequence

"""


def linear_quadratic_cubic(seq):
    first_order, second_order, third_order = [], [], []

    for i, j in zip(seq, seq[1:]):
        first_order.append(j - i)

    if len(set(first_order)) == 1:
        return "linear"

    for i, j in zip(first_order, first_order[1:]):
        second_order.append(j - i)

    if len(set(second_order)) == 1:
        return "quadratic"

    for i, j in zip(second_order, second_order[1:]):
        third_order.append(j - i)

    if len(set(third_order)) == 1:
        return "cubic"

    return "else"


def main():
    seq = list(map(int, input("Enter a sequence of space-separated integers: ").split()))
    print(linear_quadratic_cubic(seq))


if __name__ == "__main__":
    main()
