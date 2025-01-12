"""

Write a Python program to find the majority element from a given array of size n using the Collections module.

[10, 10, 20, 30, 40, 10, 20, 10]    =>  10

"""

from collections import Counter


def main():
    c = Counter([10, 10, 20, 30, 40, 10, 20, 10])
    print(c.most_common(1)[0][0])


if __name__ == "__main__":
    main()
