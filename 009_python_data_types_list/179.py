"""

Write a Python program to create the largest possible number using the elements of a given list of positive integers.

[3, 40, 41, 43, 74, 9]      =>  9744341403
[10, 40, 20, 30, 50, 60]    =>  605040302010
[8, 4, 2, 9, 5, 6, 1, 0]    =>  98654210

"""

from itertools import permutations


def main():
    data = [
        [3, 40, 41, 43, 74, 9],
        [10, 40, 20, 30, 50, 60],
        [8, 4, 2, 9, 5, 6, 1, 0]
    ]

    for _ in data:
        tmp = list("".join(_) for _ in permutations(list(map(str, _)), len(_)))
        print(max(tmp, key=int))


if __name__ == "__main__":
    main()
