"""

Write a Python program to check if the letters in a given string can be rearranged. This is to make sure that two
characters that are adjacent to each other are different using the heap queue algorithm.

Given a string s with lowercase repeated characters, the task is to rearrange characters in a string so that no two
adjacent characters are the same. If it is not possible to do so, then print empty string ("").

Note: Multiple valid rearranged strings can be possible for same input string.

"aab"       =>  aba
"abc"       =>  abc
"aabb"      =>  abab
"abccdd"    =>  cdabcd
"aa"        =>  N/A     (it's not possible to rearrange the chars in a way where adjacent chars are non-duplicates)
"aaaabc"    =>  N/A

"""

from collections import Counter
from heapq import heapify, heappop, heappush


def rearrange(s: str) -> str:
    counts = [(-count, char) for char, count in Counter(s).items()]  # max-heap -> -count
    heapify(counts)

    res, prev = "", (0, "")

    # process each char and temporarily remove it from the heap so we don't generate duplicate chars
    while counts:
        count, char = heappop(counts)  # temporarily remove the most frequent char
        res += char  # add it to the result

        # if the previously added char has a remaining repetitions -> push it to the heap
        if prev[0] < 0:
            heappush(counts, prev)

        # make the current char as the previous char and decrease its count by one
        prev = (count + 1, char)

    # the string can be rearranged only if we get the same number of characters
    if len(res) == len(s):
        return res
    else:
        return "N/A"


def main():
    data = [
        "aab",
        "abc",
        "aabb",
        "abccdd",
        "aa",
        "aaaabc"
    ]

    for _ in data:
        print(rearrange(_))


if __name__ == "__main__":
    main()
