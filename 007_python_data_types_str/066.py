"""

Write a Python program to get the total number of characters to delete from both strings in order to make two given
strings (lower case, may or may not be of the same length) anagrams.

An anagram of a string is another string that contains the same characters, only the order of characters can be
different.

spearmk, pearsuv    =>  spear, pears

"""

from collections import Counter


def main():
    str1 , str2 = input("Enter the two strings comma-separated: ").split(", ")

    # Create maps for each string
    str1_map1 = dict(Counter(str1))
    str2_map2 = dict(Counter(str2))

    ctr = 0

    # Loop through keys in second map
    for key in str2_map2.keys():
        # If key not in first map, add to counter
        if key not in str1_map1:
            ctr += str2_map2[key]
        # Else add difference
        else:
            ctr += max(0, str2_map2[key] - str1_map1[key])

    # Loop through keys in first map
    for key in str1_map1.keys():
        # If key not in second map, add to counter
        if key not in str2_map2:
            ctr += str1_map1[key]
        # Else add difference
        else:
            ctr += max(0, str1_map1[key] - str2_map2[key])

    print(ctr)


if __name__ == "__main__":
    main()
