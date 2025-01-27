"""

Write a Python program to interleave two lists into another list randomly. Use the map() function

nums1 = [1, 2, 7, 8, 3, 7]
nums2 = [4, 3, 8, 9, 4, 3, 8, 9]

[4, 3, 8, 1, 2, 9, 4, 7, 8, 3, 3, 8, 9, 7]

"""

import random


def main():
    random.seed(0)

    nums1 = [1, 2, 7, 8, 3, 7]
    nums2 = [4, 3, 8, 9, 4, 3, 8, 9]

    iterators = [iter(nums1)] * len(nums1) + [iter(nums2)] * len(nums2)
    print(list(map(next, random.sample(iterators, k=len(nums1) + len(nums2)))))


if __name__ == "__main__":
    main()
