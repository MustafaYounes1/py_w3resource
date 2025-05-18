"""

Write a Python program to find the three largest integers from a given list of numbers using the heap queue algorithm.

[25, 35, 22, 85, 14, 65, 75, 22, 58]

the three smallest integers     =>      [14, 22, 22]
the three largest integers      =>      [85, 75, 65]

"""

from heapq import nlargest, nsmallest


def main():
    lst = [25, 35, 22, 85, 14, 65, 75, 22, 58]

    print(nsmallest(3, lst))
    print(nlargest(3, lst))


if __name__ == "__main__":
    main()
