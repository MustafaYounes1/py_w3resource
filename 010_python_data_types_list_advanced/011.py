"""

Write a Python function to find the longest common sub-sequence in two lists.

[1, 2, 3, 4, 5, 6, 7, 8]
[6, 7, 5, 6, 7, 8]

=>  [5, 6, 7, 8]

[3, 5, 1, 8, 8]
[3, 3, 5, 3, 8]

=>  [3, 5]

[1, 3, 5, 7]
[2, 4, 6, 8]

=>  []

[1, 3, 5, 7]
[1, 2, 4, 6, 8]

=>  [1]

"""

from difflib import SequenceMatcher


def main():
    data = [
        [
            [1, 2, 3, 4, 5, 6, 7, 8],
            [6, 7, 5, 6, 7, 8]
        ],
        [
            [3, 5, 1, 8, 8],
            [3, 3, 5, 3, 8]
        ],
        [
            [1, 3, 5, 7],
            [2, 4, 6, 8]
        ],
        [
            [1, 3, 5, 7],
            [1, 2, 4, 6, 8]
        ]
    ]

    for lst1, lst2 in data:
        matcher = SequenceMatcher(isjunk=None, a=lst1, b=lst2)
        match = matcher.find_longest_match(0, len(lst1), 0, len(lst2))
        print(lst1[match.a: match.a + match.size])


if __name__ == "__main__":
    main()
