"""

Find the indices of the maximum and minimum values in a list.

e.g.    [5, 2, 8, 1, 7]

Minium index: 3
Maximum index: 2

"""


def main():
    lst = [5, 2, 8, 1, 7]
    print(f"Minium index: {lst.index(min(lst))}")
    print(f"Maximum index: {lst.index(max(lst))}")


if __name__ == "__main__":
    main()
