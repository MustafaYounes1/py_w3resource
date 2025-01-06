"""

Write a Python program to test if a variable is a list, tuple, or set.

"""


def main():
    ll = []
    print(isinstance(ll, list))

    tt = ()
    print(isinstance(tt, tuple))

    ss = set()
    print(isinstance(ss, set))


if __name__ == "__main__":
    main()
