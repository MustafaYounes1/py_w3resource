"""

Write a Python program to add three given lists using Python map and lambda.

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]

[12, 15, 18]

"""


def main():
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    nums3 = [7, 8, 9]
    print(list(map(sum, zip(nums1, nums2, nums3))))


if __name__ == "__main__":
    main()
