"""

Write a Python program to sort an unsorted array of numbers using Wiggle sort.

Imagine you have a line of numbers, and you want them to form a pattern where each number goes: “low, high, low, high,”
and so on. That’s Wiggle Sort!

Given an unsorted array nums, reorder it in-place such that :
    nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, if you have: [3, 5, 2, 1, 6, 4], you can reorder it to [3, 5, 1, 6, 2, 4] to make it wiggle!

Time Complexity:    O(n)
Space Complexity:   O(1)

"""


def wiggle_sort(lst: list[...]) -> None:
    """Implement the wiggle sort"""
    for i in range(1, len(lst)):
        if (i % 2 != 0 and lst[i] < lst[i - 1]) or (i % 2 == 0 and lst[i] > lst[i - 1]):
            lst[i], lst[i - 1] = lst[i - 1], lst[i]


def main():
    lst = [3, 5, 2, 1, 6, 4]
    wiggle_sort(lst)
    print(lst)


if __name__ == "__main__":
    main()
