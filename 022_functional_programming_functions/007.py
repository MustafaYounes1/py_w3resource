"""

Write a Python function that accepts a string and counts the number of upper and lower case letters.

'The quick Brow Fox'

No. of Upper case characters : 3
No. of Lower case Characters : 12

"""


def count_upper_and_lowers(s: str) -> tuple[int, int]:
    n_u, n_l = 0, 0

    for _ in s:
        if _.isupper():
            n_u += 1
        elif _.islower():
            n_l += 1
        else:
            ...

    return n_u, n_l


def main():
    print(count_upper_and_lowers("The quick Brow Fox"))


if __name__ == "__main__":
    main()
