"""

[Weird exercise]

Write a Python program to generate a palindrome of a given length from a string.
Input: madam , 7        =>  madaadam
Input: madam , 6        =>  maddam
Input: madam , 5        =>  maaaam
Input: madam , 3        =>  maam
Input: madam , 2        =>  mm
Input: madam , 1        =>  aa

"""

__data = [
    ("madam", 7),
    ("madam", 6),
    ("madam", 5),
    ("madam", 3),
    ("madam", 2),
    ("madam", 1),
]


def main():
    for s, l in __data:
        s_index = 0
        # Calculate the half length of the palindrome
        length_half = (l - (l % 2)) // 2
        ans = ""

        # Build the first half of the palindrome
        while len(ans) < length_half:
            ans += s[s_index % len(s)]
            s_index += 1

        # Add a middle character if the length is odd
        if l % 2 == 1:
            ans += "a"

        # Complete the palindrome by adding the reversed first half
        print(ans + ans[::-1])


if __name__ == "__main__":
    main()
