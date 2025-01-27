"""

Write a Python program to add two given lists and find the difference between them. Use the map() function.

nums1 = [6, 5, 3, 9]
nums2 = [0, 1, 7, 7]

[(6, 6), (6, 4), (10, -4), (16, 2)]

"""


def main():
    nums1 = [6, 5, 3, 9]
    nums2 = [0, 1, 7, 7]
    print(list(map(lambda a, b: (a + b, a - b), nums1, nums2)))


if __name__ == "__main__":
    main()
