"""

Write a Python program to check, for each string in a given list, whether the last character is an isolated letter or
not. Return True otherwise False.

Input:
['cat', 'car', 'fear', 'center']
Output:
[False, False, False, False]

Input:
['ca t', 'car', 'fea r', 'cente r']
Output:
[True, False, True, True]

"""


__data = [
    ['cat', 'car', 'fear', 'center'],
    ['ca t', 'car', 'fea r', 'cente r']
]


def main():
    for seq in __data:
        print([w[-1] == w.split(" ")[-1] for w in seq])


if __name__ == "__main__":
    main()
