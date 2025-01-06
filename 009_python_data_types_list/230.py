"""

Write a Python program to find the indices of all elements in the given list that satisfy the provided testing function.

func = [1, 2, 3, 4]
f = lambda n: n % 2 == 1

[0, 2]

"""


def main():
    lst = [1, 2, 3, 4]
    func = lambda n: n % 2 == 1

    print([idx for idx, _ in enumerate(lst) if func(_)])


if __name__ == "__main__":
    main()
