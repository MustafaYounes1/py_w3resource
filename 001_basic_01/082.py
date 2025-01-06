"""

Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary).

"""


def main():
    tt = (1, 2, 3)
    ll = [1, 2, 3]
    ss = {1, 2, 3}
    dd = {
        1: 2,
        2: 3,
        3: 3
    }

    print(f"Tuple:  {sum(tt)}")
    print(f"List:   {sum(ll)}")
    print(f"Set:    {sum(ss)}")
    print(f"Dict:   {sum(dd)}")


if __name__ == "__main__":
    main()
