"""

Write a Python program to find the index of the last element in the given list that satisfies the provided testing
function.

list = [1, 2, 3, 4]
func = lambda n: n % 2 == 1

2

"""


def main():
    lst = [1, 2, 3, 4]
    func = lambda n: n % 2 == 1

    gen = (idx for idx, _ in enumerate(lst[::-1]) if func(_))
    print(len(lst) - 1 - next(gen))


if __name__ == "__main__":
    main()
