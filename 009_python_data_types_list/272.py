"""

Write a Python program to generate a list of numbers in the arithmetic progression starting with the given positive
integer and up to the specified limit.

An Arithmetic progression (AP) or arithmetic sequence is a sequence of numbers such that the difference between the
consecutive terms is constant. For instance, the sequence 5, 7, 9, 11, 13, 15, . . . is an arithmetic progression with
a common difference of 2.

If the initial term of an arithmetic progression is a1 and the common difference of successive members is d, then the
nth term of the sequence (an) is given by:  an = a1 + (n - 1)d

Note: consider the first element a1 the same as d

1, 15   =>  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
3, 37   =>  [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
5, 25   =>  [5, 10, 15, 20, 25]

"""


def main():
    data = [
        [1, 15],
        [3, 37],
        [5, 25]
    ]

    for s, e in data:
        print(list(range(s, e + 1, s)))


if __name__ == "__main__":
    main()
