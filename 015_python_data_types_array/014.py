"""

Write a Python program to find out if a given array of singed integers contains any duplicate elements.
Return true if any value appears at least twice in the array, and return false if every element is distinct.

[1, 2, 3, 4, 5]               =>  False
[1, 2, 3, 4, 4]               =>  True
[1, 1, 2, 2, 3, 3, 4, 4, 5]   =>  True

"""

from array import array


def main():
    data = [
        array('i', [1, 2, 3, 4, 5]),
        array('i', [1, 2, 3, 4, 4]),
        array('i', [1, 1, 2, 2, 3, 3, 4, 4, 5]),
    ]

    for arr in data:
        print(not (len(arr) == len(set(arr))))


if __name__ == "__main__":
    main()
