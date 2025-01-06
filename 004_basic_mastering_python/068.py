"""

Check if a string is a palindrome. (if it remains the same on reading from both ends)

s = "racecar"   =>  True

"""


def main():
    s = "racecar"
    print(s == s[::-1])


if __name__ == "__main__":
    main()
