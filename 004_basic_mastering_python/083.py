"""

Check if a list is a palindrome

lst = [1, 2, 3, 2, 1]   =>  True

"""


def main():
    lst = [1, 2, 3, 2, 1]
    print(lst == lst[::-1])


if __name__ == "__main__":
    main()
