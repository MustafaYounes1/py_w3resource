"""

Write a Python program that removes all duplicate elements from a signed-integer array and returns a new array.

[1, 3, 5, 1, 3, 7, 9]   =>  [1, 3, 5, 7, 9]
[2, 4, 2, 6, 4, 8]      =>  [2, 4, 6, 8]
"""

from array import array


def main():
    data = [
        array('i', [1, 3, 5, 1, 3, 7, 9]),
        array('i', [2, 4, 2, 6, 4, 8])
    ]

    for arr in data:
        out = array('i', sorted(set(arr), key=arr.index))
        print(out.tolist())


if __name__ == "__main__":
    main()
