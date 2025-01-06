"""

Find the indices of non-zero elements in a list.

e.g.    lst = [1, 2, 0, 0, 4, 0]    =>  [0, 1, 4]

"""


def main():
    lst = [1, 2, 0, 0, 4, 0]
    print([idx for idx, _ in enumerate(lst) if _])


if __name__ == "__main__":
    main()
