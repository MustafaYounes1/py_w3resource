"""

Write a Python program to find the longest common prefix string among a given array of strings.
Return an empty string if there is no common prefix.

For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".
Sample Input:
["abcdefgh","abcefgh"]      => abc
["w3r","w3resource"]        => w3r
["Python","PHP", "Perl"]    => p
["Python","PHP", "Java"]    => ""

"""


def find_prefix(seq):
    prefix = ""
    sorted_seq = sorted(seq, key=lambda x: len(x))

    for idx in range(len(sorted_seq[0])):
        for w in sorted_seq[1:]:
            if sorted_seq[0][idx] != w[idx]:
                return prefix

        prefix += sorted_seq[0][idx]

    return prefix


def main():
    seq = input("Enter the words space-separated: ").split()
    print(find_prefix(seq))


if __name__ == "__main__":
    main()
