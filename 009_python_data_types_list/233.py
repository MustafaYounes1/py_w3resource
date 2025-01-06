"""

Write a Python program to chunk a given list into n smaller lists.

[1, 2, 3, 4, 5, 6, 7], 4

[[1, 2], [3, 4], [5, 6], [7]]

"""

from math import ceil


def main():
    lst, n_lists = [1, 2, 3, 4, 5, 6, 7], 4
    sub_lst_size = ceil(len(lst) / n_lists)
    print(
        list(
            map(lambda x: lst[x * sub_lst_size:x * sub_lst_size + sub_lst_size], range(n_lists))
        )
    )


if __name__ == "__main__":
    main()
