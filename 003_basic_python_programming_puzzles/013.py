"""

Write a Python program to find strings in a given list starting with a given prefix.

Input:
(ca, ('cat', 'car', 'fear', 'center'))
Output:
['cat', 'car']

Input:
(do, ('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))
Output:
['dog', 'donut']

"""

__data = [
    ('ca', ('cat', 'car', 'fear', 'center')),
    ('do', ('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))
]


def main():
    for pfx, seq in __data:
        print([_ for _ in seq if _.startswith(pfx)])


if __name__ == "__main__":
    main()
