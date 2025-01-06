"""

Write a Python program to find the positions of all uppercase vowels (not counting Y) in even indices of a given string.

Input: w3rEsOUrcE
Output:
[6]

Input: AEIOUYW
Output:
[0, 2, 4]

"""

__vowels = 'AEIOU'


def main():
    s = input("Enter a string: ")
    print(
        [idx for idx, _ in enumerate(s) if idx % 2 == 0 and _ in __vowels]
    )

if __name__ == "__main__":
    main()
