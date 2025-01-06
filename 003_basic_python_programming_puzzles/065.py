"""

Write a Python program to shift the decimal digits n places to the left, wrapping the extra digits around.
If the shift > the number of digits in n, reverse the string.

12345 1     =>  23451
12345 2     =>  34512
12345 3     =>  45123
12345 5     =>  12345
12345 6     =>  54321

"""


def main():
    n, shift = [_ for _ in input("Enter n and shift space-separated: ").split()]
    shift = int(shift)

    if shift > len(n):
        print(n[::-1])
    else:
        print(n[shift:] + n[:shift])


if __name__ == "__main__":
    main()
