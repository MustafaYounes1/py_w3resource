"""

Write a Python program to find all words in a given string with n consonants.

Input: this is our time         => #consonants = 3, 2, 1

Number of consonants: 3
Words in the said string with 3 consonants:
['this']

Number of consonants: 2
Words in the said string with 2 consonants:
['time']

Number of consonants: 1
Words in the said string with 1 consonants:
['is', 'our']

"""

__vowels = "aieou"


def main():
    s = input("Enter a string: ")
    for _ in range(1, 4):
        print(
            f"#consonants: {_};",
            [w for w in s.split() if len([c for c in w if c.lower() not in __vowels]) == _]
        )


if __name__ == "__main__":
    main()
