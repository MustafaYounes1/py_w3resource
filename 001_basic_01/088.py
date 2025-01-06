"""

Given variables x=30 and y=20, write a Python program to print "30+20=50".

"""


def main():
    x, y = [int(_) for _ in input("Enter x and y (space-separated): ").split()]
    print(f"{x}+{y}={x+y}")


if __name__ == "__main__":
    main()
