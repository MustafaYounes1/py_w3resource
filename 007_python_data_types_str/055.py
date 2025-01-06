"""

Write a Python program to find the first repeated word in a given string.

ab ca bc ab             =>  ab
ab ca bc ab ca ab bc    =>  ab
ab ca bc ca bc          =>  ab
ab ca bc                =>  None

"""


def main():
    s = input("Enter the string: ")
    repeated_words = list(filter(lambda _: s.count(_) > 1, s.split()))
    print(repeated_words[0] if repeated_words else None)


if __name__ == "__main__":
    main()
