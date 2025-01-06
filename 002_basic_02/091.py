"""

Write a Python program to count the number of arguments in a given function.

Sample Input:
()              =>  0
(1)             =>  1
(1, 2)          =>  2
(1, 2, 3)       =>  3
(1, 2, 3, 4)    =>  4
[1, 2, 3, 4]    =>  1

"""


def f(*args, **kwargs):
    print(len(args) + len(kwargs))


def main():
    f()


if __name__ == "__main__":
    main()
