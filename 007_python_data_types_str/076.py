"""

Write a Python program to count the number of substrings from a given string of lowercase alphabets with exactly k
distinct characters.

wolf    ,  4   =>   1
mustafa ,  4   =>   3

"""


def main():
    s = input("Enter a string: ").lower()
    n = int(input("Enter the size: "))
    print(
        len(
            [s[i:i + n] for i in range(0, len(s)) if len(set(s[i:i + n])) == n]
        )
    )


if __name__ == "__main__":
    main()
