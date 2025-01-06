"""

Write a Python program to find a list of strings that have fewer total characters (including repetitions).

Input:
[['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]
Output:
['this', 'list', 'is', 'narrow']

Input:
[['Red', 'Black', 'Pink'], ['Green', 'Red', 'White']]
Output:
['Red', 'Black', 'Pink']

"""

__data = [
    [['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']],
    [['Red', 'Black', 'Pink'], ['Green', 'Red', 'White']]
]


def main():
    for sample in __data:
        print(
            min(
                sample,
                key=lambda seq: sum([len(w) for w in seq])
            )
        )


if __name__ == "__main__":
    main()
