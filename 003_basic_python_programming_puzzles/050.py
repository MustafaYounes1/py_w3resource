"""

Write a Python program to find even-length words from a given list of words and sort them by length.

Original list of words:
['Red', 'Black', 'White', 'Green', 'Pink', 'Orange']
Find the even-length words and sort them by length in the said list of words:
['Pink', 'Orange']

Original list of words:
['The', 'worm', 'ate', 'a', 'bird', 'imagine', 'that', '!', 'Absurd', '!!']
Find the even-length words and sort them by length in the said list of words:
['!!', 'bird', 'that', 'worm', 'Absurd']

"""

__data = [
    ['Red', 'Black', 'White', 'Green', 'Pink', 'Orange'],
    ['The', 'worm', 'ate', 'a', 'bird', 'imagine', 'that', '!', 'Absurd', '!!']
]


def main():
    for sample in __data:
        print(
            sorted(
                [w for w in sample if len(w) % 2 == 0], key=len
            )
        )


if __name__ == "__main__":
    main()
