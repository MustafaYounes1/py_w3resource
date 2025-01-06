"""

Write a Python program to find all the common characters in lexicographical order from two given lower case strings.
If there are no similar letters print "No common characters".

w3resource, Python and SWIFT        =>  osw
Python, PHP                         =>  p
Java, PHP                           =>  No common characters

"""


def main():
    s1, s2 = input("Enter the two strings comma-separated: ").split(", ")
    matches = "".join(sorted(set(s1.lower()) & set(s2.lower())))
    print(matches if matches else "No common characters")


if __name__ == "__main__":
    main()
