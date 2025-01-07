"""

Write a Python function to find the kth smallest element in a list.

[1, 2, 4, 3, 5, 4, 6, 9, 2, 1]

1   =>  1
2   =>  1
3   =>  2
4   =>  2
5   =>  3
6   =>  4
7   =>  5
8   =>  5
9   =>  6
10  =>  9

"""


def main():
    lst = [1, 2, 4, 3, 5, 4, 6, 9, 2, 1]
    lst.sort()
    for n in range(1, 11):
        print(f"{n:2d} =>  {lst[n - 1]:2d}")


if __name__ == "__main__":
    main()
