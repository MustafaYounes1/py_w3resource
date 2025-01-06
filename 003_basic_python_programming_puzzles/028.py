"""

Write a Python program to select a string from a given list of strings with the most unique characters.

Input:
['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
Output:
abcdefhijklmnop

Input:
['Green', 'Red', 'Orange', 'Yellow', '', 'White']
Output:
Orange

"""

__data = [
    ['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique'],
    ['Green', 'Red', 'Orange', 'Yellow', '', 'White']
]


def main():
    for sample in __data:
        print(
            max(
                sample, key=lambda w: len(set(w))
            )
        )


if __name__ == "__main__":
    main()
