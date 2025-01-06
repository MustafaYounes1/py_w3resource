"""

Find the length of the longest string in a list.

lst = ['apple', 'banana', 'cherry']     =>  6

"""


def main():
    lst = ['apple', 'banana', 'cherry']
    print(len(max(lst, key=len)))


if __name__ == "__main__":
    main()
