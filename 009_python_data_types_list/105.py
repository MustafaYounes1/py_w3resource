"""

Write a Python program to compute average of two given lists.
Note: concatenate them both and do the averaging

[1, 1, 3, 4, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 4, 5, 7, 8]

Average of two lists:
3.823529411764706

"""

from statistics import mean


def main():
    lst1 = [1, 1, 3, 4, 4, 5, 6, 7]
    lst2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]

    print(mean(lst1 + lst2))


if __name__ == "__main__":
    main()
