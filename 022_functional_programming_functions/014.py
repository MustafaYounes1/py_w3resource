"""

Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.

"The quick brown fox jumps over the lazy dog"   =>  True

"""

from string import ascii_lowercase


def is_pangram(s: str) -> bool:
    return set(s.lower()) >= set(ascii_lowercase)


def main():
    print(is_pangram("The quick brown fox jumps over the lazy dog"))


if __name__ == "__main__":
    main()
