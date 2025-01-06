"""

Write a Python program to calculate the left difference between two iterables, without filtering duplicate values.

[1, 2, 3], [1, 2, 4]    =>  [3]

"""


def main():
    lst1, lst2 = [1, 2, 3], [1, 2, 4]
    print(list(filter(lambda _: _ not in lst2, lst1)))


if __name__ == "__main__":
    main()
