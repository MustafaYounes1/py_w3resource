"""

Write a Python program to segregate 0s and 1s in an array of only 0s and 1s such that 0s comes first then the 1s.

You are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array
[Basically you have to sort the array].

Note: you're allowed to traverse the array only once.

[0, 1, 0, 1, 0, 0, 1, 1, 1, 0]  =>  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

"""


def segregate_0s_1s(lst: list[...]) -> None:
    i, j = 0, len(lst) - 1

    while i < j:
        # keep incrementing the first index while getting 0s
        # -> at the end of this while loop: i would be pointing to a 1
        while i < j and lst[i] == 0:
            i += 1

        # keep decrementing the second index while getting 1s
        # -> at the end of this while loop: j would be pointing to a 0
        while i < j and lst[j] == 1:
            j -= 1

        if i < j:
            # a swap is needed since i is pointing to 1 and j is pointing to 0
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1


def main():
    lst = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
    segregate_0s_1s(lst)
    print(lst)


if __name__ == "__main__":
    main()
