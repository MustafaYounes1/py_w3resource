"""

Write a Python program to calculate Euclid's totient function for a given integer.
Use a primitive method to calculate Euclid's totient function.

The Euler's Totient Function counts the numbers lesser than a number say n that do not share any common positive
factor other than 1 with n or in other words are co-prime with n.

Sample Input:
(10)    =>  4
(15)    =>  8
(33)    =>  20

"""


def gcd(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2

    return n1


def main():
    n = int(input("Enter a number: "))

    print(
        len(
            list(filter(lambda x: gcd(n, x) == 1, range(1, n + 1)))
        )
    )


if __name__ == "__main__":
    main()
