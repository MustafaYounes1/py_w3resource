"""

Write a Python program that creates a 'Counter' for a list of words and removes all items with a count less than a
certain value.

["Red", "Green", "Black", "Black", "Red", "red", "Orange", "Pink", "Pink", "Red", "White"]
min_count = 2

-> Counter({'red': 4, 'black': 2, 'pink': 2})

"""

from collections import Counter


def main():
    lst = ["Red", "Green", "Black", "Black", "Red", "red", "Orange", "Pink", "Pink", "Red", "White"]
    min_count = 2

    c = Counter(map(lambda w: w.lower(), lst))
    c = Counter({w: cnt for w, cnt in c.items() if cnt >= min_count})
    print(c)


if __name__ == "__main__":
    main()
