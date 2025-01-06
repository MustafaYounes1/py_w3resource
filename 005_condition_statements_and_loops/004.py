"""

 Write a Python program to construct the following pattern, using a nested for loop.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

"""


def main():
    for i in range(1, 10):
        for j in range(0, i if i <= 5 else 10 - i):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    main()
