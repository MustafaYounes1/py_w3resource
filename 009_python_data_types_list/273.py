"""

Write a Python program to find an element that divides a given list of integers with the same sum value.

[0, 9, 2, 4, 5, 6]      =>  4
[-4, 0, 6, 1, 0, 2]     =>  1
[1, 2, 3, 4]            =>  No such element!
[-4, 0, 5, 1, 0, 1]     =>  1

"""


def main():
    data = [
        [0, 9, 2, 4, 5, 6],
        [-4, 0, 6, 1, 0, 2],
        [1, 2, 3, 4],
        [-4, 0, 5, 1, 0, 1]
    ]

    for lst in data:
        for idx, _ in enumerate(lst):
            if sum(lst[:idx]) == sum(lst[idx + 1:]):
                print(_)
                break
        else:
            print("No such element!")


if __name__ == "__main__":
    main()
