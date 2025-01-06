"""

Write a Python program to remove duplicate characters from a given string.

python exercises practice solution  =>  python exrcisalu
w3resource                          =>  w3resouc

"""

from collections import OrderedDict


def main():
    s = input("Enter a string: ")
    d = OrderedDict.fromkeys(s)
    print("".join(d.keys()))


if __name__ == "__main__":
    main()
