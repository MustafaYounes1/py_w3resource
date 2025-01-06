"""

Write a Python program to compute the sum of digits of each number in a given list.

[10, 2, 56]   (1+0+2+5+6)       =>  14
[10, 20, 4, 5, 'b', 70, 'a']    =>  19
[10, 20, -4, 5, -70]            =>  19

"""


def main():
    data = [
        [10, 2, 56],
        [10, 20, 4, 5, 'b', 70, 'a'],
        [10, 20, -4, 5, -70]
    ]

    for _ in data:
        print(sum([int(___) for __ in _ for ___ in str(__) if ___.isdigit()]))


if __name__ == "__main__":
    main()
