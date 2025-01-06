"""

Write a Python program to find the index of the largest prime in the list and the sum of its digits.

Input: [3, 7, 4]                                                            =>  [1, 7]
Input: [3, 11, 7, 17, 19, 4]                                                =>  [4, 10]
Input: [23, 17, 201, 14, 10473, 43225, 421, 423, 11, 10, 2022, 342157]      =>  [6, 7]

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
    res = [(idx, _) for idx, _ in enumerate(seq) if is_prime(_)]
    res = max(res, key=lambda x: x[1])
    print(
        [res[0], sum([int(_) for _ in str(res[1])])]
    )


if __name__ == "__main__":
    main()
