"""

Write a Python program to create a 24-hour time format (HH:MM) using the 4 given digits. Display the latest time and
do not use any digit more than once.

[1, 2, 3, 4]    =>  23:41
[1, 2, 4, 5]    =>  21:54
[2, 2, 4, 5]    =>  22:54
[2, 2, 4, 3]    =>  23:42
[0, 2, 4, 3]    =>  23:40

"""

from itertools import permutations


def main():
    data = [
        [1, 2, 3, 4],
        [1, 2, 4, 5],
        [2, 2, 4, 5],
        [2, 2, 4, 3],
        [0, 2, 4, 3]
    ]

    for _ in data:
        t = max(
            filter(
                lambda __: (0 <= int(__[:2]) < 24) and (0 <= int(__[2:]) < 60),
                map("".join, permutations(map(str, _)))
            )
        )
        assert len(t) == 4, "Invalid input"
        print(f"{t[:2]}:{t[2:]}")


if __name__ == "__main__":
    main()
