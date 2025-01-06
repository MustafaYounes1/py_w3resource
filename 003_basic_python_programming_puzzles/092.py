"""

Write a Python program to sort the elements at the even indices in an input list.
Note: keep the elements at odd indices untouched

[2, 5, 6, 3, 1, 4, 34]              =>  [1, 5, 2, 3, 6, 4, 34]
[8, 0, 7, 2, 9, 4, 1, 2, 8, 3]      =>  [1, 0, 7, 2, 8, 4, 8, 2, 9, 3]


"""


def swap(ll, ii, jj):
    tmp = ll[ii]
    ll[ii] = ll[jj]
    ll[jj] = tmp


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))

    for idx in range(0, len(seq), 2):
        for j in range(idx, len(seq), 2):
            if seq[idx] > seq[j]:
                swap(seq, idx, j)

    print(seq)


if __name__ == "__main__":
    main()
