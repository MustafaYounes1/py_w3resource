"""

Write a Python program to find a string consisting of space-separated characters with given counts.

Input: {'f': 1, 'o': 2}             =>  f o o
Input: {'a': 1, 'b': 1, 'c': 1}     =>  a b c

"""

__data = [
    {'f': 1, 'o': 2},
    {'a': 1, 'b': 1, 'c': 1}
]


def main():
    for sample in __data:
        print(" ".join(k for k, v in sample.items() for _ in range(v)))


if __name__ == "__main__":
    main()
