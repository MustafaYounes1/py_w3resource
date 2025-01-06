"""

Write a Python program that reads an integer n and finds the number of combinations of a,b,c and d
(0 = a,b,c,d = 9) where (a + b + c + d) will be equal to n.

Input:
n (1 ≤ n ≤ 50)
    Input the number(n):    15
    Number of combinations: 592

"""

from itertools import product


def main():
    n = int(input("Enter a number: "))

    res = 0
    r = [_ for _ in range(10)]
    for p in product(r, r, r, r):
        if sum(p) == n:
            res += 1

    print(res)


if __name__ == "__main__":
    main()
