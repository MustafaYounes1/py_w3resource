"""

Write a Python program to find the longest common ending between two given strings.

Original strings: running ruminating                =>  ing
Original strings: thisisatest testing123testing     =>  ""

"""


def find_longest_common_ending(s1, s2):
    res = ""

    for l1, l2 in zip(s1[::-1], s2[::-1]):
        if l1 == l2:
            res += l1
        else:
            break

    return res[::-1]


def main():
    s1, s2 = input("Enter two space-separated words: ").split()
    print(find_longest_common_ending(s1, s2))


if __name__ == "__main__":
    main()
