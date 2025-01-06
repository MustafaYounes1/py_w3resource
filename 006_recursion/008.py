"""

Write a Python program to calculate the sum of harmonic series upto n terms.
Note: The harmonic sum is the sum of reciprocals of the positive integers.
Example : 1 + 1/2 + 1/3 + 1/4 + 1/5 + ...

7   =>  2.5928571428571425
4   =>  2.083333333333333

"""


def harmonic_series(n):
    if n <= 1:
        return 1

    return (1 / n) + harmonic_series(n - 1)


def main():
    n = int(input("Enter a number: "))
    print(harmonic_series(n))


if __name__ == "__main__":
    main()
