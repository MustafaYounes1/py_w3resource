"""

Write a Python program to get the length of a float array [5.5, 4.0, 7.9].

    =>  3

"""

from array import array


def main():
    arr = array('f', [5.5, 4.0, 7.9])
    print(len(arr))
    # or
    # print(arr.buffer_info()[1])


if __name__ == "__main__":
    main()
