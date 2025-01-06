"""

Write a Python program to find all integers <= 1000 that are the product of exactly three primes. Each integer
should be represented as a list of its three prime factors.

Input: 10
Output:
[[2, 2, 2]]

Input: 50
Output:
[
    [2, 2, 2], [2, 2, 3], [2, 2, 5], [2, 2, 7], [2, 2, 11], [2, 3, 2], [2, 3, 3], [2, 3, 5], [2, 3, 7], [2, 5, 2],
    [2, 5, 3], [2, 5, 5], [2, 7, 2], [2, 7, 3], [2, 11, 2], [3, 2, 2], [3, 2, 3], [3, 2, 5], [3, 2, 7], [3, 3, 2],
    [3, 3, 3], [3, 3, 5], [3, 5, 2], [3, 5, 3], [3, 7, 2], [5, 2, 2], [5, 2, 3], [5, 2, 5], [5, 3, 2], [5, 3, 3],
    [5, 5, 2], [7, 2, 2], [7, 2, 3], [7, 3, 2], [11, 2, 2]
]

"""


def main():
    n = int(input("Enter a number: "))
    ps = [p for p in range(2, n) if all(p % sat != 0 for sat in range(2, p))]
    print([[p, q, r] for p in ps for q in ps for r in ps if p * q * r <= n])


if __name__ == "__main__":
    main()
