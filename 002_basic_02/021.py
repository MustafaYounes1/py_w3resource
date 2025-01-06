"""

Write a Python program to find the number of notes (Samples of notes: 10, 20, 50, 100, 200, 500) against an amount.
Range - Number of notes(n) : n (1 <= n <= 1000000).

e.g.:
    880     =>  500 + 200 + 100 + 50 + 20 + 10  (6 notes)
    1000    =>  500 + 500                       (2 notes)


Define a function 'no_notes' that calculates the minimum number of notes required to represent a given amount 'a'
using denominations of 500, 200, 100, 50, 20, and 10.

f there is any remaining amount not covered by the available denominations/notes return -1

"""


def get_n_notes(n):
    notes = [500, 200, 100, 50, 20, 10]

    res = 0
    for note in notes:
        res += n // note
        n = n % note

    if n > 0:
        res = -1

    return res


def main():
    n = int(input("Enter the number: "))
    print(get_n_notes(n))


if __name__ == "__main__":
    main()
