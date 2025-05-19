"""

Write a Python program to find a triplet in an array such that the sum is closest to a given number. Return the sum of
the three integers.

[1, 2, 3, 4, 5, -6], 14     ->  (3, 4, 5) 12
[1, 2, 3, 4, -5, -6], 5     ->  (1, 2, 3) 6
[-1, 2, 2, 4], 4            ->  (-1, 2, 4) 5

"""


def triplet_with_closest_sum(lst: list[int], target: int) -> tuple[int, int, int] | None:
    """Two-pointer approach"""
    res: tuple[int, int, int] | None = None

    if len(lst) < 3:
        return res

    sorted_lst = sorted(lst)  # sort the array in ascending order
    closest_sum = float("inf")  # the current sum

    # iterate through possible first items in the output triplet
    for i in range(len(sorted_lst) - 2):
        left_p, right_p = i + 1, len(lst) - 1  # initialize two pointers: left and right

        while left_p < right_p:
            curr_triplet = (sorted_lst[i], sorted_lst[left_p], sorted_lst[right_p])  # current triplet
            curr_sum = sum(curr_triplet)  # current sum

            # if the current triplet's sum equals to the target -> return the current triplet
            if curr_sum == target:
                return curr_triplet

            # if the current triplet's sum is closer to the target -> update the closet sum and the output triplet
            if abs(curr_sum - target) < abs(closest_sum - target):
                closest_sum = curr_sum
                res = curr_triplet

            # if the current triplet's sum is larger that the target -> look for smaller sum -> move right_p to the left
            if curr_sum > target:
                right_p -= 1

            # otherwise -> look for larger sum -> move left_p to the right
            else:
                left_p += 1

    return res


def main():
    data = [
        [[1, 2, 3, 4, 5, -6], 14],
        [[1, 2, 3, 4, -5, -6], 5],
        [[-1, 2, 2, 4], 4]
    ]

    for lst, s in data:
        closed_t = triplet_with_closest_sum(lst, s)
        assert closed_t is not None, "Can't form triplets from the input list"
        print(closed_t, sum(closed_t))


if __name__ == "__main__":
    main()
