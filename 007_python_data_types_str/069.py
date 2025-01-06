"""

Write a Python program to find the longest common sub-string from two given strings.

abcdefgh, xswerabcdwd           =>  abcd
15sd45asdmusss2sss, 1545musss   =>  musss

"""

from difflib import SequenceMatcher


def main():
    s1, s2 = input("Enter two comma-separated strings: ").split(", ")

    matcher = SequenceMatcher(isjunk=None, a=s1, b=s2)

    # get all matches
    # The last triple is a dummy, and has the value (len(a), len(b), 0)
    # each match is a triple is of the form (i, j, n), and means that a[i:i+n] == b[j:j+n].
    # it's a named tuple where i is named a, j is named b, abd n is named size
    all_matches = [s1[match.a: match.a + match.size] for match in matcher.get_matching_blocks()[:-1]]

    print(max(all_matches, key=len))

    # or you can use for a more efficient performance
    # find_longest_match(alo=0, ahi=None, blo=0, bhi=None)
    # Finds the longest matching block in a[alo:ahi] and b[blo:bhi].

    # match = seq_match.find_longest_match(0, len(s1), 0, len(s2))
    # s1[match.a: match.a + match.size]


if __name__ == "__main__":
    main()
