"""

Write a Python program for sequential search.
    Return -1 if the item does not exist, otherwise return its index

In computer science, linear search or sequential search is a method for finding a particular value in a list that
checks each element in sequence until the desired element is found or the list is exhausted. The list need not be
ordered. (Time complexity: O(n))

Time complexity:    O(n).
Space complexity:   O(1).


[11, 23, 58, 31, 56, 77, 43, 12, 65, 19], 31    ->  3
[4, 45, 3, -2, 4, 80], 100                      ->  -1

"""


def linear_search(lst: list[...], obj: object) -> int:
    for idx, _ in enumerate(lst):
        if _ == obj:
            return idx

    return -1


def main():
    data = [
        ([11, 23, 58, 31, 56, 77, 43, 12, 65, 19], 31),
        ([4, 45, 3, -2, 4, 80], 100)
    ]

    for lst, item in data:
        print(linear_search(lst, item))


if __name__ == "__main__":
    main()
