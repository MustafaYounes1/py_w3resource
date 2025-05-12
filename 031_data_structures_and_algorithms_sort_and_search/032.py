"""

Write a Python program to sort unsorted strings using natural sort.

Natural sort order is an ordering of strings in alphabetical order, except that multi-digit numbers are treated
atomically, i.e., as if they were a single character.

Natural sort order has been promoted as being more human-friendly ("natural") than the machine-oriented pure alphabetical
order. For example, in alphabetical sorting "z11" would be sorted before "z2" because "1" is sorted as smaller than "2",
while in natural sorting "z2" is sorted before "z11" because "2" is sorted as smaller than "11".

['Elm11', 'Elm12', 'Elm2', 'elm0', 'elm1', 'elm10', 'elm13', 'elm9']

Ascending order:    ['elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13']
Descending order:   ['elm13', 'Elm12', 'Elm11', 'elm10', 'elm9', 'Elm2', 'elm1', 'elm0']

"""

import re


def natural_key(s: str) -> list[str | int]:
    """Split the string around each sequence of consecutive digits, while considering each consecutive sequence of
    digits as one single number:
        e.g. '0_foo_452_s' -> ['', 0, '_foo_', 452, '_s']
    """
    return [int(part) if part.isdigit() else part for part in re.split(r"([0-9]+)", s)]


def natural_sort(lst: list[str], reverse: bool = False) -> None:
    """An implementation of natural sort"""

    lst.sort(
        key=lambda s: (
            # 1st key: convert the string to a list formed after interpreting consecutive digits as one number
            natural_key(s.lower()),

            # 2nd key: follow lexicographical order when two items are considered equal,
            # e.g., '10_e' = 010_e' according to the above key, however, '010_e' should come first in the natural sort.
            s,
        ),
        reverse=reverse
    )


def main():
    lst = ['Elm11', 'Elm12', 'Elm2', 'elm0', 'elm1', 'elm10', 'elm13', 'elm9']
    lst1 = lst[:]  # a shallow copy

    natural_sort(lst, False)
    print(lst)

    natural_sort(lst1, True)
    print(lst1)


if __name__ == "__main__":
    main()
