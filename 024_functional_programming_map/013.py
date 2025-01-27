"""

Write a Python program to count the same pair in two given lists. use map() function.

nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
nums2 = [2, 2, 3, 1, 2, 6, 7, 9]

> 4

"""

from operator import eq


def main():
    nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
    nums2 = [2, 2, 3, 1, 2, 6, 7, 9]
    print(sum(list(map(eq, nums1, nums2))))


if __name__ == "__main__":
    main()
