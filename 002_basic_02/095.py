"""

Write a Python program that checks whether every even index contains an even number and every odd index contains an
odd number of a given list.

Original list of numbers: [2, 1, 4, 3, 6, 7, 6, 3]      =>  True

Original list of numbers: [2, 1, 4, 3, 6, 7, 6, 4]      =>  False

"""


def is_even(n):
    return n % 2 == 0


def main():
    seq = list(map(int, input("Enter a list of space-separated numbers: ").split()))

    print(
        all(seq[i] % 2 == i % 2 for i in range(len(seq)))
    )


if __name__ == "__main__":
    main()
