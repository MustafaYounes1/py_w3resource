"""

Write a Python program to check whether a given string is a number or not using Lambda.

"26587"         =>  True
"4.2365"        =>  True
"-12547"        =>  True
"00"            =>  True
"A001"          =>  False
"001"           =>  True
"-16.4"         =>  True
"-24587.11"     =>  True

"""

from typing import Callable


def main():
    is_numeric: Callable[[str], bool] = lambda s: s.replace(".", "", 1).replace("-", "", 1).replace("+", "", 1).isdigit()
    print(is_numeric("26587"))
    print(is_numeric("4.2365"))
    print(is_numeric("-12547"))
    print(is_numeric("00"))
    print(is_numeric("A001"))
    print(is_numeric("001"))
    print(is_numeric("-16.4"))
    print(is_numeric("-24587.11"))


if __name__ == "__main__":
    main()
