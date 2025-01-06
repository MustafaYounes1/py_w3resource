"""

Write a Python program that prints each item and its corresponding type from the following list.

Sample List :
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

"""


def main():
    lst = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
    for _ in lst:
        print(_, type(_))


if __name__ == "__main__":
    main()
