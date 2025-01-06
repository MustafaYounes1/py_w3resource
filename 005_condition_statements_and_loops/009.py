"""

Write a Python program to get the Fibonacci series between 0 and 50.
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34

"""


def main():
    fibs = [0, 1]

    for _ in range(2, 50):
        f = fibs[-2] + fibs[-1]

        if f >= 50:
            break
        else:
            fibs.append(f)

    print(" ".join(list(map(str, fibs[1:]))))


if __name__ == "__main__":
    main()
