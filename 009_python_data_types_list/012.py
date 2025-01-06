"""

Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']

"""


def main():
    lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    print([_ for idx, _ in enumerate(lst) if idx not in (0, 4, 5)])


if __name__ == "__main__":
    main()
