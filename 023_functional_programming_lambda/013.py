"""

Write a Python program to count the even and odd numbers in a given array of integers using Lambda.

[1, 2, 3, 5, 7, 8, 9, 10]
Number of even numbers in the above array: 3
Number of odd numbers in the above array: 5

"""


def main():
    lst = [1, 2, 3, 5, 7, 8, 9, 10]
    print(len(list(filter(lambda _: _ % 2 == 0, lst))))
    print(len(list(filter(lambda _: _ % 2 != 0, lst))))


if __name__ == "__main__":
    main()
