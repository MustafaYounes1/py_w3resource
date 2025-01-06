"""

Write a Python program to find the following strange sort of list of numbers:

the first element is the smallest,
the second is the largest of the remaining,
the third is the smallest of the remaining,
the fourth is the largest of the remaining,
etc. (smallest -> largest)

[1, 3, 4, 5, 11]        =>  [1, 11, 3, 5, 4]
[27, 3, 8, 5, 1, 31]    =>  [1, 31, 3, 27, 5, 8]
[1, 2, 7, 3, 4, 5, 6]   =>  [1, 7, 2, 6, 3, 5, 4]

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    seq = sorted(seq)
    res = []
    for idx in range(len(seq) // 2):
        res.append(seq[idx])
        res.append(seq[-(idx + 1)])
    if len(seq) % 2 != 0:
        res.append(seq[len(seq) // 2])
    print(res)


if __name__ == "__main__":
    main()
