"""

Write a Python program to check whether the given strings are palindromes or not. Return True otherwise False.

Input:
['palindrome', 'madamimadam', '', 'foo', 'eyes']
Output:
[False, True, True, False, False]

"""


__data = ['palindrome', 'madamimadam', '', 'foo', 'eyes']


def main():
    print(
        [_ == _[::-1] for _ in __data]
    )


if __name__ == "__main__":
    main()
