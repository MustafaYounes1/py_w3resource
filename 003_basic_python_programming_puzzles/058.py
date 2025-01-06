"""

Write a Python program to find the biggest even number between two numbers inclusive.

12, 51      =>  50
1, 79       =>  78
47, 53      =>  52
100, 200    =>  200

"""


def main():
    a, b = [int(_) for _ in input("Enter two comma-separated integers: ").split(",")]
    for _ in range(max(a, b), min(a, b) + 1, -1):
        if _ % 2 == 0:
            print(_)
            break


if __name__ == "__main__":
    main()
