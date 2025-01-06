"""

Write a Python program to count the number of carry operations for each addition problem.
According to Wikipedia " In elementary arithmetic, a carry is a digit that is transferred from one column of digits
to another column of more significant digits. It is part of the standard algorithm to add numbers together by starting
with the rightmost digits and working to the left. For example, when 6 and 7 are added to make 13, the "3" is written
to the same column and the "1" is carried to the left".

    786, 457    =>  3
    5, 6        =>  1
"""


def n_carries(a, b):
    a, b = str(a), str(b)

    i = 0
    n = 0
    while i < len(a) or i < len(b):
        if int(a[-i]) + int(b[-i]) >= 10:
            n += 1
        i += 1

    return n


def main():
    a, b = [int(_) for _ in input("Enter two space-separated numbers: ").split()]
    print(n_carries(a, b))

if __name__ == "__main__":
    main()
