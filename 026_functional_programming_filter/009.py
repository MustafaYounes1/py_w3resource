"""

Write a Python function that filters out elements from a list of strings containing a specific substring using the
filter function.

['Red', 'Green', 'Orange', 'White', 'Black', 'Pink', 'Yellow'], "l"     =>  ['Black', 'Yellow']

"""


def main():
    lst, s = ['Red', 'Green', 'Orange', 'White', 'Black', 'Pink', 'Yellow'], "l"
    print(list(filter(lambda _: s in _, lst)))


if __name__ == "__main__":
    main()
