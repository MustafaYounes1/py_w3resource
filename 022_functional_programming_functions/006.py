"""

Write a Python function to check whether a number falls within a given range.

5 in [3, 9[     =>  True

"""


def check_in(n: int, r: range) -> bool:
    return n in r


def main():
    print(check_in(5, range(3, 9)))


if __name__ == "__main__":
    main()
