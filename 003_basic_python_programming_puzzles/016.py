"""

Write a Python program to find strings in a given list containing a given substring.

Input:
(ca,('cat', 'car', 'fear', 'center'))
Output:
['cat', 'car']

Input:
(o,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))
Output:
['dog', 'donut', 'todo']

Input:
(oe,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))
Output:
[]

"""


__data = [
    ('ca', ('cat', 'car', 'fear', 'center')),
    ('o', ('cat', 'dog', 'shatter', 'donut', 'at', 'todo', '')),
    ('oe', ('cat', 'dog', 'shatter', 'donut', 'at', 'todo', '')),
]


def main():
    for sub_str, seq in __data:
        print([_ for _ in seq if sub_str in _])


if __name__ == "__main__":
    main()
