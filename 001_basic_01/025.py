"""

Write a Python program that checks whether a specified value is contained within a group of values.

Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False

"""


def main():
    seq = [int(_) for _ in input("Input a list of space-separated integers: ").split()]
    n = int(input("Input the value: "))
    if n in seq:
        print(f"{n} is in {seq}")
    else:
        print(f"{n} is in not {seq}")


if __name__ == "__main__":
    main()
