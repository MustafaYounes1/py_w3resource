"""

Write a Python program to check if a given string contains an element that is present in a list.

'https://www.w3resource.com/python-exercises/list/', ['.com', '.edu', '.tv']    =>  True
'https://www.w3resource.net', ['.com', '.edu', '.tv']                           =>  False

"""


def main():
    data = [
        ['https://www.w3resource.com/python-exercises/list/', ['.com', '.edu', '.tv']],
        ['https://www.w3resource.net', ['.com', '.edu', '.tv']]
    ]

    for s, lst in data:
        print(any(_ in s for _ in lst))


if __name__ == "__main__":
    main()
