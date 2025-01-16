"""

Write a Python program to create an array of six unsigned integers [10, 20, 30, 40, 50, 60].
Print all members of the array on one line

10 20 30 40 50 60

"""

from array import array


def main():
    arr = array('I', [10, 20, 30, 40, 50, 60])
    for _ in arr:
        print(_, end=" ")


if __name__ == "__main__":
    main()
