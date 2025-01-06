"""

Write a Python program to generate a list containing the Fibonacci sequence, up until the nth term.

First 7 Fibonacci numbers:
[0, 1, 1, 2, 3, 5, 8]

First 15 Fibonacci numbers:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

First 50 Fibonacci numbers: [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181,
6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887,
9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170,
1836311903, 2971215073, 4807526976, 7778742049]

"""


def fib(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return fib(n - 1) + fib(n - 2)


def main():
    data = [7, 15, 50]

    for n in data:
        res = [0, 1]

        while len(res) < n:
            res.append(res[-1] + res[-2])

        print(res)


if __name__ == "__main__":
    main()
