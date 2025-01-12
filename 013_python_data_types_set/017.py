"""

Write a Python program to check if two given sets have no elements in common.

x = {1, 2, 3, 4}
y = {4, 5, 6, 7}
z = {8}

x and y     =>  False
x and z     =>  True
y and z     =>  True

"""


def main():
    x = {1, 2, 3, 4}
    y = {4, 5, 6, 7}
    z = {8}

    # alternatively, you can use x.isdisjoint(y)
    # True if none of the items are present in both sets, otherwise it returns False.
    print(not (x & y))
    print(not (x & z))
    print(not (y & z))


if __name__ == "__main__":
    main()
