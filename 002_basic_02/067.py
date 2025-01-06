"""

From Wikipedia,
A happy number is defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process
until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.

Write a Python program to find and print the first 10 happy numbers.
Sample Input:   [:10]
Sample Output:  [1, 7, 10, 13, 19, 23, 28, 31, 32, 44]

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
    n = int(input("Enter a number: "))

    res, curr_number = [], 1

    while len(res) != n:
        if is_happy(curr_number):
            res.append(curr_number)

        curr_number += 1

    print(res)

if __name__ == "__main__":
    main()
