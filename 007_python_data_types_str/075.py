"""

Write a Python program to find the smallest window that contains all characters in a given string.

asdaewsqgtwwsa      =>  daewsqgt
aabcbcdbca          =>  dbca
muuusssddddrqrrz    =>  muuusssddddrqrrz
"""

import re


def main():
    s = input("Enter a string: ")
    chars = "".join(set(s))

    non_greedy_pattern = "(?=(" + f".*?".join([f"[{chars}]" for _ in range(len(chars))]) + "))"
    greedy_pattern = "(?=(" + f".*".join([f"[{chars}]" for _ in range(len(chars))]) + "))"

    # find all matches (greedy + non-greedy) sometimes the non-greedy matches would contain matches that doesn't have
    # all the characters
    matches = set(re.findall(non_greedy_pattern, s) + re.findall(greedy_pattern, s))

    # find the matches that have all characters
    matches = list(filter(lambda m: len(set(m)) == len(chars), matches))

    # find the match with the smallest length
    print(min(matches, key=len))


if __name__ == "__main__":
    main()
