"""

Write a Python program to check whether all dictionaries in a list are empty or not.

[{},{},{}]        =>  True
[{1,2},{},{}]     =>  False

"""


def main():
    lst =[{1,2},{},{}]
    print(all(not _ for _ in lst))


if __name__ == "__main__":
    main()
