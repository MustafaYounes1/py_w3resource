"""

Write a Python program to calculate the sum of a list of numbers using recursion.

[2, 4, 5, 6, 7]     =>  24

"""


def sum_using_recursion(l):
    if not l:
        return 0
    else:
        return l[0] + sum_using_recursion(l[1:])


def main():
    lst = [2, 4, 5, 6, 7]
    print(sum_using_recursion(lst))


if __name__ == "__main__":
    main()
