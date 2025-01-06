"""

Internet search engine giant, such as Google accepts web pages around the world and classify them, creating a huge
database. The search engines also analyze the search keywords entered by the user and create inquiries for database
search. In both cases, complicated processing is carried out in order to realize efficient retrieval, but basics are
all cutting out words from sentences.

Write a Python program to cut out / return words of 3 to 6 characters length from a given sentence not more
than 1024 characters.

Input:
English sentences consisting of delimiters and alphanumeric characters are given on one line.
Input a sentence (1024 characters. max.)
The quick brown fox => The quick brown fox

"""


def main():
    s = input("Enter a string: ").strip().split()
    res = [word for word in s if 3 <= len(word) <= 6]
    print(" ".join(res))


if __name__ == "__main__":
    main()
