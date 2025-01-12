"""

Write a Python program to check if a set is a subset of another set.

x = {'mango', 'apple'}
y = {'mango', 'orange'}
z = {'mango'}

If x is subset of y     =>  False
If y is subset of x     =>  False
If y is subset of z     =>  False
If z is subset of y     =>  True

"""


def main():
    x = {'mango', 'apple'}
    y = {'mango', 'orange'}
    z = {'mango'}

    print(x <= y)
    print(y <= x)
    print(y <= z)
    print(z <= y)


if __name__ == "__main__":
    main()
