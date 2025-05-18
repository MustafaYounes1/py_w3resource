"""

Write a Python program that deletes the smallest element from a heap and then inserts a new item.

[25, 44, 68, 21, 39, 23, 89]

Pop and insert 21
Pop and insert 110

->  [23, 25, 68, 44, 39, 110, 89]

"""

from heapq import heapify, heapreplace


def main():
    lst = [25, 44, 68, 21, 39, 23, 89]

    heapify(lst)
    heapreplace(lst, 21)  # equivalent to heappop -> heapreplace; but more efficient
    heapreplace(lst, 110)

    print(lst)


if __name__ == "__main__":
    main()
