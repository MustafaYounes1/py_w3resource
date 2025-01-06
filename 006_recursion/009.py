"""

Write a Python program to calculate the geometric sum up to 'n' terms.
Note: In mathematics, a geometric series is a series with a constant ratio between successive terms.

sum(1 / 2^m) for m in the range: [0, n]

7   =>  1.9921875
4   =>  1.9375

"""


def geo_series(n):
    if not n:
        return 1

    return 1 / pow(2, n) + geo_series(n - 1)


def main():
    n = int(input("Enter a number: "))
    print(geo_series(n))


if __name__ == "__main__":
    main()
