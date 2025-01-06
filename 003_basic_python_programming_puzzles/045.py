"""

Write a Python program to find all even palindromes up to n.
Note: An integer is a palindrome when it reads the same backward as forward. Negative numbers are not palindromic.

Even palindromes up to 50
[0, 2, 4, 6, 8, 22, 44]

Even palindromes up to 100
[0, 2, 4, 6, 8, 22, 44, 66, 88]

Even palindromes up to 500
[
    0, 2, 4, 6, 8, 22, 44, 66, 88, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 404, 414, 424, 434, 444, 454, 464,
    474, 484, 494
]

Even palindromes up to 2000
[
    0, 2, 4, 6, 8, 22, 44, 66, 88, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 404, 414, 424, 434, 444, 454,
    464, 474, 484, 494, 606, 616, 626, 636, 646, 656, 666, 676, 686, 696, 808, 818, 828, 838, 848, 858, 868, 878, 888,
    898
]

"""


def main():
    n = int(input("Enter a number: "))
    print([i for i in range(0, n, 2) if str(i) == str(i)[::-1]])


if __name__ == "__main__":
    main()
