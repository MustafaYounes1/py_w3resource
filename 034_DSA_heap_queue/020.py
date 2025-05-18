"""

Write a Python program to create a LIFO queue (Stack), add 0 -> 9 to the stack, and get them one by one.

9 8 7 6 5 4 3 2 1 0

"""

from queue import LifoQueue

def main():
    q = LifoQueue()

    for _ in range(10):
        q.put_nowait(_)

    while not q.empty():
        print(q.get_nowait(), end=" ")


if __name__ == "__main__":
    main()
