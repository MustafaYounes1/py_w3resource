"""

Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

{'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

['b', 'e', 'c']

"""


def main():
    d = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
    print(sorted(d, key=d.get, reverse=True)[:3])

    # or you can use the heapq nlargest
    # nlargest(n, d, key=d.get)


if __name__ == "__main__":
    main()
