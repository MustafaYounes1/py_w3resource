"""

Write a Python program to create the next bigger number by rearranging the digits of a given number.

12  =>  21
10  =>  None
201 =>  210
102 =>  120
445 =>  454

"""

from itertools import permutations


def main():
    data = [12, 10, 201, 102, 445]
    for _ in data:
        nums = sorted(map(lambda _: int("".join(_)), permutations(str(_), len(str(_)))))
        print(nums[nums.index(_) + 1] if nums.index(_) + 1 < len(nums) else None)


if __name__ == "__main__":
    main()
