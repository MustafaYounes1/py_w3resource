"""

Write a Python program to create a bytearray from a list.

"""


def main():
    ll = [1, 2, 3, 4, 5, 255]
    # he bytearray class is a mutable sequence of integers in the range 0 <= x < 256. I
    ba = bytearray(ll)

    print(ba)

    for _ in ba:
        print(_)


if __name__ == "__main__":
    main()
