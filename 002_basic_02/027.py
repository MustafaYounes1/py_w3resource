"""

Write a Python program to find the type of the progression (arithmetic progression / geometric progression) and
the next successive member of the three successive members of a sequence.

According to Wikipedia, an arithmetic progression (AP) is a sequence of numbers such that the difference of any
two successive members of the sequence is a constant. For instance, the sequence 3, 5, 7, 9, 11, 13, ... is an
arithmetic progression with common difference 2. For this problem, we will limit ourselves to arithmetic progression
whose common difference is a non-zero integer.

On the other hand, a geometric progression (GP) is a sequence of numbers where each term after the first is found by
multiplying the previous one by a fixed non-zero number called the common ratio. For example, the sequence 2, 6, 18,
54, ... is a geometric progression with common ratio 3. For this problem, we will limit ourselves to geometric
progression whose common ratio is a non-zero integer.

    [1, 2, 3]       =>  4
    [2, 6, 18]      =>  54.0
    [0, 0, 0]       =>  Wrong Numbers (neither AP nor GP)

"""


def find_next(seq):
    assert len(seq) >= 3, "Expected a list of at least 3 integers"

    if (seq[1] - seq[0]) == (seq[2] - seq[1]) and (seq[1] - seq[0]) > 0:
        return seq[2] + (seq[1] - seq[0])

    elif seq[0] > 0 and seq[1] > 0 and (seq[1] / seq[0]) == (seq[2] / seq[1]):
        return seq[2] * (seq[1] / seq[0])

    else:
        raise ValueError("Wrong numbers")


def main():
    seq = [int(_) for _ in input("Enter a list of space-separated integers: ").split()]
    try:
        print(find_next(seq))

    except ValueError as err:
        print(err)


if __name__ == "__main__":
    main()
