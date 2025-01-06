"""

Write a Python program to find the position of the second occurrence of a given string in another given string.
If there is no such string return -1.
Sample Input:
("The quick brown fox jumps over the lazy dog", "the")  =>  -1
("the quick brown fox jumps over the lazy dog", "the")  =>  31

"""


def find_second(doc: str, s: str):
    return doc.find(s, doc.find(s) + 1)


def main():
    doc = input("Enter the document: ")
    s = input("Enter the string: ")
    print(find_second(doc, s))


if __name__ == "__main__":
    main()
