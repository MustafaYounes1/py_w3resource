"""

Given an array of numbers representing a branch on a binary tree, write a Python program to find the minimum even
value and its index. In the case of a tie, return the smallest index. If there are no even numbers, the answer is [].

Input:
[1, 9, 4, 6, 10, 11, 14, 8]
Output:
Minimum even value and its index of the said array of numbers:
[4, 2]

Input:
[1, 7, 4, 4, 9, 2]
Output:
Minimum even value and its index of the said array of numbers:
[2, 5]

Input:
[1, 7, 7, 5, 9]
Output:
Minimum even value and its index of the said array of numbers:
[]

"""


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    evens = [_ for _ in seq if _ % 2 == 0]
    if evens:
        print([min(evens), seq.index(min(evens))])
    else:
        print([])



if __name__ == "__main__":
    main()
