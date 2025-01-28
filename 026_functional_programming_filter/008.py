"""

Write a Python program that creates a list of words and use the filter function to extract words that contain more
than five letters.

['Red', 'Green', 'Orange', 'White', 'Black', 'Pink', 'Yellow']     =>   ['Orange', 'Yellow']

"""


def main():
    lst = ['Red', 'Green', 'Orange', 'White', 'Black', 'Pink', 'Yellow']
    print(list(filter(lambda _: len(_) > 5, lst)))


if __name__ == "__main__":
    main()
