"""

Given a list, and an integer target, find all possible unique quadruplets in the list whose sum is equal to the
given target value. We can return quadruplets in any order, but all the quadruplets should be internally sorted, i.e.,
for any quadruplets [q1, q2, q3, q4] the following should follow: q1 <= q2 <= q3 <= q4.

[-2, -1, 1, 2, 3, 4, 5, 6], 10
    =>  [(-2, 1, 5, 6), (-2, 2, 4, 6), (-2, 3, 4, 5), (-1, 1, 4, 6), (-1, 2, 3, 6), (-1, 2, 4, 5), (1, 2, 3, 4)]

[10, 2, 3, 4, 5, 7, 8], 23
    =>  [(2, 3, 8, 10), (2, 4, 7, 10), (3, 5, 7, 8)]

"""


def get_quadruplets(lst: list[int], target: int) -> list[tuple[int, int, int, int]] | None:
    """Find unique quadruplets that sum to a predefined target using the two-pointer approach"""
    res: list[tuple[int, int, int, int]] = []

    if len(lst) < 4:
        return None

    lst = sorted(lst)

    # i is the index of the first number in the quadruplet
    for i in range(len(lst) - 3):

        # skip duplicates for i
        if (i > 0) and (lst[i] == lst[i - 1]):
            continue

        # j is the index of the first number in the quadruplet
        for j in range(i + 1, len(lst) - 2):

            # skip duplicates for j
            if (j > i + 1) and (lst[j] == lst[j - 1]):
                continue

            # initialize two pointers: left pointer (third element) and right pointer (fourth element)
            k, l = j + 1, len(lst) - 1

            while k < l:
                quadruplet = (lst[i], lst[j], lst[k], lst[l])
                curr_sum = sum(quadruplet)

                if curr_sum == target:
                    res.append(quadruplet)

                    # move the left pointer one step to the right and the left pointer one step to the left
                    k += 1
                    l -= 1

                    # skip duplicates for k
                    while (k < l) and (lst[k] == lst[k - 1]):
                        k += 1

                    # skip duplicates for l
                    while (k < l) and (lst[l] == lst[l + 1]):
                        l -= 1

                # if the current quadruplet's sum is larger that the target -> look for smaller sum
                # -> move k to the left
                elif curr_sum > target:
                    l -= 1

                # otherwise -> look for larger sum -> move k to the right
                else:
                    k += 1

    return res


def main():
    data = [
        [[-2, -1, 1, 2, 3, 4, 5, 6], 10],
        [[10, 2, 3, 4, 5, 7, 8], 23],
    ]

    for lst, target in data:
        print(get_quadruplets(lst, target))


if __name__ == "__main__":
    main()
