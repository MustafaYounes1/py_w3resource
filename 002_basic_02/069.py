"""

In abstract algebra, a group isomorphism is a function between two groups that sets up a one-to-one correspondence
between the elements of the groups in a way that respects the given group operations. If there exists an isomorphism
between two groups, then the groups are called isomorphic.

Two strings are isomorphic if the characters in string A can be replaced to get string B
Given "foo", "bar", return false.
Given "paper", "title", return true.

Isomorphic strings are strings where each character in one string can be consistently replaced with another character
to result in the second string. (for both strings)

Write a Python program to check if two given strings are isomorphic to each other or not.
Sample Input:
("foo", "bar")      => False
("bar", "foo")      => False    (first 'o' in 'foo' is replaced with 'a' from 'bar', but the second replaces 'r')
("paper", "title")  => True
("title", "paper")  => True
("apple", "orange") => False
("aa", "ab")        => False
("ab", "aa")        => False

"""


def is_isomorphic(s: str, t: str) -> bool:
    # Create two arrays to store the last seen positions of characters
    # from strings 's' and 't'.
    last_seen_s, last_seen_t = [0] * 256, [0] * 256

    # Iterate over the characters of the strings 's' and 't' simultaneously.
    for index, (char_s, char_t) in enumerate(zip(s, t), 1):  # Starting from 1
        # Convert the characters to their ASCII values
        ascii_s, ascii_t = ord(char_s), ord(char_t)

        # Check if the last seen positions for both characters are different.
        # If they are, then strings 's' and 't' are not isomorphic.
        if last_seen_s[ascii_s] != last_seen_t[ascii_t]:
            return False

        # Update the last seen positions for 'char_s', 'char_t' with the
        # current index which represents their new last seen position.
        last_seen_s[ascii_s] = last_seen_t[ascii_t] = index

    # If we have not found any characters with different last seen positions
    # till the end of both strings, then the strings are isomorphic.
    return True


def main():
    s1, s2 = input("Enter the two strings space-separated: ").split()
    print(isIsomorphic(s1, s2))


if __name__ == "__main__":
    main()
