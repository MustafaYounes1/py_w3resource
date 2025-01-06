"""

Write a Python program to get the single digits in numbers sorted backwards and converted into English words.

[1, 3, 4, 5, 11]        =>  ['five', 'four', 'three', 'one']
[27, 3, 8, 5, 1, 31]    =>  ['eight', 'five', 'three', 'one']

"""

__mapping = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}


def main():
    seq = list(map(int, input("Enter a list of comma-separated integers: ").split(",")))
    print(
        [__mapping.get(_) for _ in sorted(seq, reverse=True) if len(str(_)) == 1]
    )


if __name__ == "__main__":
    main()
