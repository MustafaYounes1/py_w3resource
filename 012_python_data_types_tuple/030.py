"""

Write a Python program to check if a specified element appears in a tuple of tuples.

(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))

White =>    True
Olive =>    False

"""


def main():
    lst = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
    data = ('White', 'Olive')

    for _ in data:
        print(any(_ in __ for __ in lst))


if __name__ == "__main__":
    main()
