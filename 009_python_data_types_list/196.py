"""

Write a Python program to move a specified element in a given list.

['red', 'green', 'white', 'black', 'orange']

'white'   =>  ['red', 'green', 'black', 'orange', 'white']
'red'     =>  ['green', 'white', 'black', 'orange', 'red']
'black'   =>   ['red', 'green', 'white', 'orange', 'black']

"""


def main():
    lst = ['red', 'green', 'white', 'black', 'orange']
    els = ('white', 'red', 'black')

    for e in els:
        lst_cpy = list(lst)
        lst_cpy.append(lst_cpy.pop(lst_cpy.index(e)))
        print(lst_cpy)


if __name__ == "__main__":
    main()
