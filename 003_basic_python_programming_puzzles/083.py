"""

A string is happy if every three consecutive characters are distinct. Write a Python program to find two indices
associated with a given string being unhappy.

Python      =>  None
Unhappy     =>  [4, 5]
Find        =>  None
Street      =>  [3, 4]

"""

__data = [
    "Python",
    "Unhappy",
    "Find",
    "Street"
]


def main():
    for s in __data:
        res = [[idx, idx + 1] for idx in range(len(s) - 1) if s[idx] == s[idx + 1]]

        if not res:
            print(None)
        else:
            print(res)


if __name__ == "__main__":
    main()
