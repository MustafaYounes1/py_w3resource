"""

Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words
in sorted form (alphanumerically).

Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white

"""


def main():
    s = input("Enter the sequence of words: ")
    print(", ".join(sorted(set(s.split(", ")))))


if __name__ == "__main__":
    main()
