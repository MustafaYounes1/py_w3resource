"""

A Python Dictionary contains List as a value. Write a Python program to update the list values in the said dictionary.

{'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}

Add 1 to each element of the list whose key is 'Math'
Subtract 2 of each element of the list whose key is 'Physics'

{'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}

"""


def main():
    d = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
    d['Math'] = [_ + 1 for _ in d['Math']]
    d['Physics'] = [_ -2 for _ in d['Physics']]
    print(d)


if __name__ == "__main__":
    main()
