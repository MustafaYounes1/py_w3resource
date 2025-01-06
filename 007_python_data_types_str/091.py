"""

Write a Python program to convert a given heterogeneous list of scalars into a string.

['Red', 100, -50, 'green', 'w,3,r', 12.12, False]

Red,100,-50,green,w,3,r,12.12,False

"""


def main():
    lst = ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
    print(",".join([str(_) for _ in lst]))


if __name__ == "__main__":
    main()
