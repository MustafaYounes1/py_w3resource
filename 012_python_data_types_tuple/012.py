"""

Write a Python program to remove an item from a tuple.

"w", 3, "r", "s", "o", "u", "r", "c", "e"

remove c

('w', 3, 'r', 's', 'o', 'u', 'r', 'e')

"""


def main():
    t = "w", 3, "r", "s", "o", "u", "r", "c", "e"
    el = 'c'
    idx = t.index(el)
    print(t[:idx] + t[idx+1:])


if __name__ == "__main__":
    main()
