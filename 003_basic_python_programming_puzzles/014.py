"""

Write a Python program to find the length of a given list of non-empty strings.

Input:
['cat', 'car', 'fear', 'center']
Output:
[3, 3, 4, 6]

Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
[3, 3, 7, 5, 2, 4, 0]

"""

__data = [
    ['cat', 'car', 'fear', 'center'],
    ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
]


def main():
    for _ in __data:
        print([len(__) for __ in _])


if __name__ == "__main__":
    main()
