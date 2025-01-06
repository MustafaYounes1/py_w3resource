"""

Write a Python program to find a list of all numbers that are adjacent to a prime number in the list,
sorted without duplicates.

[2, 17, 16, 0, 6, 4, 5]         =>  [2, 4, 16, 17]
[1, 2, 19, 16, 6, 4, 10]        =>  [1, 2, 16, 19]
[1, 2, 3, 5, 1, 16, 7, 11, 4]   =>  [1, 2, 3, 4, 5, 7, 11, 16]

"""

from math import sqrt


def is_prime(n):
    if n <= 1:
        return False

    for _ in range(2, int(sqrt(n)) + 1):
        if n % _ == 0:
            return False

    return True


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    print(
        sorted({
            n for i, n in enumerate(seq)
            if (i > 0 and is_prime(seq[i - 1])) or (i < len(seq) - 1 and is_prime(seq[i + 1]))
        })
    )


if __name__ == "__main__":
    main()
