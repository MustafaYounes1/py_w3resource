"""

Write a Python program to insert an element before each element of a list.

color = ['Red', 'Green', 'Black']

['c', 'Red', 'c', 'Green', 'c', 'Black']

"""


def main():
    color = ['Red', 'Green', 'Black']
    res = [_ for __ in color for _ in ('c', __)]
    print(res)


if __name__ == "__main__":
    main()
