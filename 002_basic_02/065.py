"""

In mathematics, a subsequence is a sequence that can be derived from another sequence by deleting some or no elements
without changing the order of the remaining elements. For example, the sequence (A,B,D) is a subsequence of
(A,B,C,D,E,F) obtained after removal of elements C, E, and F. The relation of one sequence being the subsequence of
another is a preorder.

The subsequence should not be confused with substring (A,B,C,D) which can be derived from the above string
(A,B,C,D,E,F) by deleting substring (E,F). The substring is a refinement of the subsequence.
The list of all subsequences for the word "apple" would be "a", "ap", "al", "ae", "app", "apl", "ape", "ale", "appl",
"appe", "aple", "apple", "p", "pp", "pl", "pe", "ppl", "ppe", "ple", "pple", "l", "le", "e", "".
Write a Python program to find the longest word in a set of words which is a subsequence of a given string.

Sample Input:
("Green", {"Gn", "Gren", "ree", "en"})          =>  Gren
("pythonexercises", {"py", "ex", "exercises"})  =>  exercises

"""


def find_longest(seq, word):
    longest_word = ""

    for w in seq:
        i = 0
        tmp_word = ""

        for c in w:
            for j in range(i, len(word)):
                if c == word[j]:
                    i = j
                    tmp_word += c
                    break

        if tmp_word == w and len(w) > len(longest_word):
            longest_word = w

    return longest_word


def main():
    seq = [word for word in input("Enter the list of words (space-separated): ").split()]
    s = input("Enter the string: ")

    print(find_longest(seq, s))


if __name__ == "__main__":
    main()
