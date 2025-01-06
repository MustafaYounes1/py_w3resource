"""

Write a Python program to compute the digit distance between two integers.
The digit distance between two numbers is the absolute value of the difference of those numbers.
For example, the distance between 3 and -3 on the number line given by the |3 - (-3) | = |3 + 3 | = 6 units
Digit distance of 123 and 256 is
Since |1 - 2| + |2 - 5| + |3 - 6| = 1 + 3 + 3 = 7

Sample Input:
(123, 256)      =>  7
(23, 56)        =>  6
(1, 2)          =>  1
(24232, 45645)  =>  11

"""


def main():
    n1, n2 = input("Enter the two number space-separated: ").split()
    print(
        sum(
            [abs(int(d1) - int(d2)) for d1, d2 in zip(n1, n2)]
        )
    )


if __name__ == "__main__":
    main()
