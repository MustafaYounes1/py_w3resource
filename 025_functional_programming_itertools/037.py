"""

Write a Python program to get the index of the first element that is greater than a specified element using the
itertools module.

[12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]

Index of the first element which is greater than 73     =>  4
Index of the first element which is greater than 21     =>  1
Index of the first element which is greater than 80     =>  5
Index of the first element which is greater than 55     =>  3

"""

from itertools import dropwhile


def main():
    lst = [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]
    nums = [73, 21, 80, 55]

    for n in nums:
        print(next(dropwhile(lambda _: _[1] <= n, enumerate(lst)))[0])


if __name__ == "__main__":
    main()
