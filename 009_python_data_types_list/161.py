"""

[Starred]

Write a Python program to check if a given list increases strictly. Moreover, if removing only one element from
the list results in a strictly increasing list, we still consider the list true.

[]                          True
[1]                         True
[1, 2]                      True
[1, 2, 3]                   True
[3, 1, 2]                   True
[1, 2, 3, 0, 4, 5, 6]       True
[1, 2, 3, 0]                True
[1, 2, 0, 3]                True
[10, 1, 2, 3, 4, 5]         True
[1, 2, 10, 3, 4]            True
[1, 2, 3, 12, 4, 5]         True
[3, 2, 1]                   False
[1, 2, 0, -1]               False
[5, 6, 1, 2]                False
[1, 2, 3, 0, -1]            False
[10, 11, 12, 2, 3, 4, 5]    False

"""


def main():
    data = [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        [3, 1, 2],
        [1, 2, 3, 0, 4, 5, 6],
        [1, 2, 3, 0],
        [1, 2, 0, 3],
        [10, 1, 2, 3, 4, 5],
        [1, 2, 10, 3, 4],
        [1, 2, 3, 12, 4, 5],
        [3, 2, 1],
        [1, 2, 0, -1],
        [5, 6, 1, 2],
        [1, 2, 3, 0, -1],
        [10, 11, 12, 2, 3, 4, 5]
    ]

    for _ in data:
        if len(_) < 3:
            print(True)
            continue

        # extended unpacking.
        a, b, *seq = _

        skipped = 0

        for c in seq:
            if a < b < c:
                a, b = b, c
                continue

            elif b < c:
                # drop a since it's the largest
                a, b = b, c

            elif a < c:
                # drop b since it's the largest
                a, b = a, c

            skipped += 1

            # if we skipped two number already, then the list is not in a strict increasing order
            # since, only deleting one number is allowed
            if skipped == 2:
                print(False)
                break

        else:
            # finally a and b should be strictly increasing
            print(a < b)

        # ##Another approach##
        # if _ == sorted(_):
        #     print(True)
        #
        # else:
        #     for idx, __ in enumerate(_[1:-1], start=1):
        #         if _[idx] - _[idx - 1] != 1 or _[idx + 1] - _[idx] != 1:
        #             for ii in [idx - 1, idx, idx + 1]:
        #                 lc = list(_)
        #                 lc.pop(ii)
        #                 if lc == sorted(lc):
        #                     print(True)
        #                     break
        #
        #             else:
        #                 print(False)
        #
        #             break


if __name__ == "__main__":
    main()
