"""

Write a Python program to find the longest string in a given list of strings.

['cat', 'car', 'fear', 'center']                        =>  center
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']    =>  shatter

"""

__data = [
    ['cat', 'car', 'fear', 'center'],
    ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
]


def main():
    for _ in __data:
        print(max(_, key=len))


if __name__ == "__main__":
    main()
