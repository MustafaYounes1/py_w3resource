"""

Write a Python program to find the vowels from each of the original texts (y counts as a vowel at the end of the word)
from a given list of strings.

Input: ['w3resource', 'Python', 'Java', 'C++']
Output:
['eoue', 'o', 'aa', '']

Input: ['ably', 'abruptly', 'abecedary', 'apparently', 'acknowledgedly']
Output:
['ay', 'auy', 'aeeay', 'aaey', 'aoeey']

"""

__data = [
    ['w3resource', 'Python', 'Java', 'C++'],
    ['ably', 'abruptly', 'abecedary', 'apparently', 'acknowledgedly']
]

__vowels = "aeiou"


def main():
    for sample in __data:
        print(
            [
                "".join([
                    _ for idx, _ in enumerate(w) if (_.lower() in __vowels) or (idx == len(w) - 1 and _.lower() == "y")
                ]) for w in sample
            ]
        )


if __name__ == "__main__":
    main()
