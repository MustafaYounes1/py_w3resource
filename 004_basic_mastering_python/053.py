"""

Find the mode of a list of numbers (the most common number that appears in your set of data).

e.g. lst = [1, 2, 2, 3, 3, 3, 4, 4]      =>  3

"""

from collections import Counter


def main():
    lst = [1, 2, 2, 3, 3, 3, 4, 4]
    print(Counter(lst).most_common(1)[0][0])


if __name__ == "__main__":
    main()
