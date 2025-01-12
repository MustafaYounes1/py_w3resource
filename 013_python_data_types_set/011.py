"""

Write a Python program to create a shallow copy of sets.

Note : Shallow copy is a bit-wise copy of an object. A new object is created that has an exact copy of the values in
the original object.

s1 = {"Red", "Green"}

create s2 as a shallow copy of s1

"""


def main():
    s1 = {"Red", "Green"}
    s2 = s1.copy()
    print(s2)


if __name__ == "__main__":
    main()
