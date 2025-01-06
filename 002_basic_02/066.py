"""

From Wikipedia, the free encyclopaedia:
A happy number is defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process
until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.

Note: If the current sum of squares has been encountered before, it forms a cycle => The number is not a Happy Number

Write a Python program to check whether a number is "happy" or not.

Sample Input:
(7)     => True
(932)   => True
(6)     => False

"""


def is_happy(n):
    past_sums = set()

    while n != 1:
        n = int(
            sum(
                [pow(int(d), 2) for d in str(n)]
            )
        )

        if n in past_sums:
            return False

        past_sums.add(n)

    return True


def main():
    n = int(input("Enter the number: "))
    print(is_happy(n))


if __name__ == "__main__":
    main()
