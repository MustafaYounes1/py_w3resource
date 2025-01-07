"""

Write a Python function to find the kth largest element in a list.

[1, 2, 4, 3, 5, 4, 6, 9, 2, 1]

1   =>  9
2   =>  6
3   =>  5
4   =>  4
5   =>  4
6   =>  3
7   =>  2
8   =>  2
9   =>  1
10  =>  1

"""


def main():
    lst = [1, 2, 4, 3, 5, 4, 6, 9, 2, 1]
    lst.sort(reverse=True)
    for n in range(1, 11):
        print(f"{n:2d} =>  {lst[n - 1]:2d}")


if __name__ == "__main__":
    main()
