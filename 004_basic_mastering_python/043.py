"""

Calculate the pairwise Euclidean distance between two lists.

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

5.196152422706632

"""

from math import sqrt


def main():
    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]
    print(
        sqrt(
            sum([pow(lst1[i] - lst2[i], 2) for i in range(3)])
        )
    )


if __name__ == "__main__":
    main()
