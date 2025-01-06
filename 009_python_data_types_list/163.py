"""

Write a Python program to get the index of the first element that is greater than a specified element.

[12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]

Index of the first element which is greater than 73     =>  4
Index of the first element which is greater than 21     =>  1
Index of the first element which is greater than 80     =>  5
Index of the first element which is greater than 55     =>  3

"""


def main():
    lst = [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]
    nums = [73, 21, 80, 55]

    for _ in nums:
        # for idx, __ in enumerate(lst):
        #     if __ > _:
        #         print(idx)
        #         break
        # else:
        #     print(f"All numbers are equal to or smaller than {_}")

        # or in a neater way
        valid_idx_gen = (idx for idx, __ in enumerate(lst) if __ > _)
        print(next(valid_idx_gen))


if __name__ == "__main__":
    main()
