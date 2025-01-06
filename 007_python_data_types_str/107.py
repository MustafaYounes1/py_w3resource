"""

Write a Python program that takes two strings. Count the number of times each string contains the same three
letters at the same index.

Red, RedGreen            -> 1
Red White, Red White     -> 7
Red White, White Red     -> 0

"""


def main():
    s1, s2 = input("Enter two comma-separated strings: ").split(", ")
    matches = [s1[idx: idx + 3] for idx in range(0, len(s1) - 2) if s1[idx: idx + 3] == s2[idx: idx + 3]]
    print(len(matches), matches)


if __name__ == "__main__":
    main()
