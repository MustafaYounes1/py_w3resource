"""

Write a Python program to find the index of the first element in the given list that satisfies the provided testing
function.

[1, 2, 3, 4], n is odd, 0

"""


def main():
    lst = [1, 2, 3, 4]
    odd_idx_gen = (idx for idx, _ in enumerate(lst) if _ % 2 != 0)
    print(next(odd_idx_gen))


if __name__ == "__main__":
    main()
