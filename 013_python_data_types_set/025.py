"""

Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the
first and vice versa.

{1, 2, 3, 4, 5, 6}
{3, 4, 5, 6, 7, 8}

Missing numbers in the second set as compared to the first  =>  {1, 2}
Missing numbers in the first set as compared to the second  =>  {8, 7}

"""


def main():
    s1 = {1, 2, 3, 4, 5, 6}
    s2 = {3, 4, 5, 6, 7, 8}

    print(s1 - s2)
    print(s2 - s1)


if __name__ == "__main__":
    main()
