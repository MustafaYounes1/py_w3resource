"""

Write a Python function that takes two arguments and returns their sum if both aren't None, otherwise return None.

sum_()          =>  None
sum_(1)         =>  None
sum_(1, 2)      =>  3

"""

def sum_(a: int | None = None, b: int | None = None) -> int | None:
    if (a is not None) and (b is not None):
        return a + b
    else:
        return None


def main():
    print(sum_())
    print(sum_(1))
    print(sum_(1, 2))


if __name__ == "__main__":
    main()
