"""

Write a Python program to find three integers which give the sum of zero in a given array of integers using Binary
Search (bisect).

[-20, 0, 20, 40, -20, -40, 80]          => [[-40, 0, 40], [-20, -20, 40], [-20, 0, 20]]
[1, 2, 3, 4, 5, -6]                     => [[-6, 1, 5], [-6, 2, 4]]
[-4, -1, 1, 2, 3]                       => [[-4, 1, 3]]
[0, -1, 2, -3, 1]                       => [[-3, 1, 2], [-1, 0, 1]]
[1, -2, 1, 0, 5]                        => [[-2, 1, 1]]
[2, 3, 1, 0, 5]                         => []

"""

from bisect import bisect_left, bisect_right
from collections import Counter


def zero_sum_triplets(lst: list[int]) -> list[list[int]]:
    res = []

    if len(lst) < 3:
        return res

    counts = Counter(lst)
    nums = sorted(counts.keys())  # sort the unique nums in ascending order

    # loop through the unique sorted numbers until the first positive number
    for i, num in enumerate(nums):

        if num < 0:
            # num is repeated -> check [num, num, -2 * num]
            if (counts[num] > 1) and (-2 * num in counts):
                res.append([num, num, -2 * num])

            # check for [num, a, b] where a, b could be equal or different

            # find a and b such that (num + a + b = 0) => a + b = -num
            ab_sum = -num

            # find the range of possible indices for a

            # since (a + b = ab_sum), theoretically, the largest value b can take is nums[-1]
            # -> the lowest value a can take is (a = ab_sum - nums[-1])
            a_lo = bisect_left(nums, ab_sum - nums[-1], i+1)

            # to avoid duplicates, e.g., [-4, 1, 3], [-4, 3, 1], we would be interested in 'a' values such that a <= b
            # -> the maximum value a could take is (ab_sum // 2)
            a_hi = bisect_right(nums, ab_sum // 2, a_lo)

            # loop through possible value of a
            for a in nums[a_lo: a_hi]:
                b = ab_sum - a

                # b should be in the list, and if it equals to 'a', the count should be bigger than one
                if (b in counts) and (a != b or counts[a] > 1):
                    res.append([num, a, b])

        # possible solution [0, 0, 0]
        elif num == 0 and counts[num] > 2:
            res.append([0, 0, 0])

        # got a positive number -> found all possible solutions already (if there are any) -> stop executing
        else:
            break

    return res


def main():
    data = [
        [-20, 0, 20, 40, -20, -40, 80],
        [1, 2, 3, 4, 5, -6],
        [-4, -1, 1, 2, 3],
        [0, -1, 2, -3, 1],
        [1, -2, 1, 0, 5],
        [2, 3, 1, 0, 5]
    ]

    for lst in data:
        print(zero_sum_triplets(lst))


if __name__ == "__main__":
    main()
