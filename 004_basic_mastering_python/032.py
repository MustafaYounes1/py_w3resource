"""

Find the indices of the top N maximum values in a list.

lst = [10, 5, 8, 20, 15]
n = 2

[3, 4]

"""


def main():
    lst = [10, 5, 8, 20, 15]
    n = 2
    print(
        [lst.index(_) for _ in sorted(lst, reverse=True)[:n]]
    )


if __name__ == "__main__":
    main()
