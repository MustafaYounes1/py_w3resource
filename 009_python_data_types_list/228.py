"""

Write a Python program to get every element that exists in any of the two given lists once, after applying the
provided function to each element of both.

[4.1], [2.2, 4.3], floor    =>  [2.2, 4.1]

"""

from math import floor


def main():
    lst1, lst2 = [4.1], [2.2, 4.3]
    print(
        list(
            set(
                lst1 + [_ for _ in lst2 if floor(_) not in set(map(floor, lst1))]
            )
        )
    )


if __name__ == "__main__":
    main()
