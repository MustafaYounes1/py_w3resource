"""

Find the unique values and their counts in a list.

e.g.    lst = [1, 2, 3, 2, 4, 1, 5, 4, 6]

        Value: 1, count: 2
        Value: 2, count: 2
        Value: 3, count: 1
        Value: 4, count: 2
        Value: 5, count: 1
        Value: 6, count: 1

"""

from collections import Counter


def main():
    lst = [1, 2, 3, 2, 4, 1, 5, 4, 6]
    for v, c in Counter(lst).items():
        print(f"Value: {v}, count: {c}")


if __name__ == "__main__":
    main()
