"""

Write a Python program to count and display vowels in text.

w3resource

e 2
o 1
u 1

"""


def main():
    s = "w3resource"
    for _ in "aeiou":
        if _ in s:
            print(_, s.lower().count(_))


if __name__ == "__main__":
    main()
