"""

Write a Python program to sort a list of 0s, 1s, and 2s using the Dutch National Flag Algorithm.

Given an array consisting of only 0s, 1s, and 2s. The task is to sort the array, i.e., put all 0s first, then all 1s
and all 2s in last.

This problem is the same as the famous “Dutch National Flag problem”. The problem was proposed by Edsger Dijkstra.
The problem is as follows: Given n balls of colour red, white or blue arranged in a line in random order. You have to
arrange all the balls such that the balls with the same colours are adjacent with the order of the balls, with the
order of the colours being red, white and blue (i.e., all red coloured balls come first then the white coloured balls
and then the blue coloured balls).

Note: You're allowed to traverse the input list only once.

[0, 1, 2, 0, 1, 2, 0, 1, 2, 0]  =>  [0, 0, 0, 0, 1, 1, 1, 2, 2, 2]

"""


def dutch_national_flag(lst: list[...]) -> None:
    i = j = 0
    k = len(lst) - 1

    # i would start at 0 and move to the right as we get a 0
    # k would start at the last index and move to the left as we get 2
    # j is the index of the current item
    #   swap it with lst[i] if the current item is 0
    #   swap it with lst[k] if the current item is 2

    # at the end of this function call #
    # lst[0: i]   ->  0s
    # lst[i: j]   ->  1s
    # lst[k+1:]   ->  2s

    while j <= k:

        # if the current item is 0
        if lst[j] == 0:
            # swap between the current item and the item at i
            lst[i], lst[j] = lst[j], lst[i]

            # both i and j should go one step to the right
            i += 1
            j += 1

        # if the current item is 1
        elif lst[j] == 1:
            j += 1  # j should go step to the right

        # if the current item is 2
        else:
            # swap between the current item and the item at k
            lst[j], lst[k] = lst[k], lst[j]
            k -= 1  # k should go one step to the left
            # note that j shouldn't be moved to the right here, it could become a 0 now -> so we need to check it again


def main():
    lst = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
    dutch_national_flag(lst)
    print(lst)


if __name__ == "__main__":
    main()
